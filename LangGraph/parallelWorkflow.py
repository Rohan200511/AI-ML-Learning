import os

from dotenv import load_dotenv
load_dotenv()
from typing import TypedDict , Annotated
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph , START , END

llm = ChatGroq(
    model="qwen/qwen3.6-27b",
    temperature=0.1
)

def merge_score_dicts(existing : dict , newupdated : dict) -> dict:   #TODO Reducers
    if existing is None:
        return newupdated
    
    return {**existing , **newupdated}

#===============
# ^STATE
#==============

class AnalyzerState(TypedDict):
    raw_text : str
    safety_scores : Annotated[dict[str : int] , merge_score_dicts]
    

#============
# ~Nodes
#============

def toxicity_node(state: AnalyzerState) -> dict:
    print("\n [Branch 1] Analyzing Toxicity and Hate Speech...")
    prompt = (
        "Analyze the following text for profanity, aggression, hate speech, or toxicity. "
        "Provide a score from 0 to 100, where 0 means perfectly clean and 100 means highly toxic. "
        "Return ONLY the plain integer number, nothing else.\n\n"
        f"Text:\n{state['raw_text']}"
    )
    response = llm.invoke(prompt)
    try:
        score = int(response.content.strip())
    except ValueError:
        score = 0
        

    return {"safety_scores": {"toxicity_level": score}}

def copyright_node(state: AnalyzerState) -> dict:
    print("\n🔏 [Branch 2] Analyzing Copyright & Originality Risks...")
    prompt = (
        "Analyze the following text. Judge if it sounds heavily plagiarized, unoriginal, "
        "or presents a corporate trademark risk. Provide a score from 0 to 100, "
        "where 0 means entirely original and 100 means high risk. "
        "Return ONLY the plain integer number, nothing else.\n\n"
        f"Text:\n{state['raw_text']}"
    )
    response = llm.invoke(prompt)
    try:
        score = int(response.content.strip())
    except ValueError:
        score = 0

    return {"safety_scores": {"copyright_risk": score}}


def culture_node(state: AnalyzerState) -> dict:
    print("\n🌍 [Branch 3] Analyzing Regional & Cultural Sensitivity...")
    prompt = (
        "Analyze the following text for regional sensitivities, political landmines, "
        "or cultural insensitivity that might offend a global audience. Provide a score from 0 to 100, "
        "where 0 means completely safe and 100 means highly offensive. "
        "Return ONLY the plain integer number, nothing else.\n\n"
        f"Text:\n{state['raw_text']}"
    )
    response = llm.invoke(prompt)
    try:
        score = int(response.content.strip())
    except ValueError:
        score = 0

    return {"safety_scores": {"cultural_insensitivity": score}}

#=========
# &Graph
#========

graph = StateGraph(AnalyzerState)


graph.add_node("toxicity_node" , toxicity_node)
graph.add_node("copyright_check" , copyright_node)
graph.add_node("cultural_node" , culture_node)

graph.add_edge(START,"toxicity_node")
graph.add_edge(START,"copyright_check")
graph.add_edge(START,"cultural_node")

graph.add_edge("toxicity_node",END)
graph.add_edge("copyright_check",END)
graph.add_edge("cultural_node",END)


app = graph.compile()

sample_script = """
    Yo guys! Welcome back to the stream. Today I am going to show you how to hack into 
    your friend's system using a script I copied directly from an online forum. 
    Honestly, traditional security protocols are absolute garbage and anyone still using 
    them is an absolute idiot. Let's dive into the code!
    """
    
initial_state = {
    "raw_text": sample_script,
    "safety_scores": {} #* Initialized as an empty dictionary
}
    
final_state = app.invoke(initial_state)
    

print(final_state["safety_scores"])