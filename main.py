# Unit 2.1 The smolagents framework
from smolagents import (
    CodeAgent, ToolCallingAgent, LiteLLMModel, tool, Tool, load_tool,
    DuckDuckGoSearchTool, VisitWebpageTool, FinalAnswerTool
)
from langfuse import get_client
from openinference.instrumentation.smolagents import SmolagentsInstrumentor
from tools.league_table_tool import LeagueTableTool
from langchain_community.agent_toolkits.load_tools import load_tools
from PIL import Image

### Langfuse Telemetry Setup ###
langfuse = get_client()
if langfuse.auth_check():
    print("Langfuse client is authenticated and ready!")
else:
    print("Authentication failed. Please check your credentials and host.")

SmolagentsInstrumentor().instrument()

### Local LLM Setup ###
model = LiteLLMModel(
    model_id="ollama_chat/qwen2:7b",
    api_base="http://127.0.0.1:11434",
    num_ctx=8192,
)

### Tools ###
@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggests a menu based on the occasion.
    Args:
        occasion: The type of occasion for the party.
    """
    if occasion == "casual":
        return "Pizza, snacks, and drinks."
    elif occasion == "formal":
        return "3-course dinner with wine and dessert."
    elif occasion == "superhero":
        return "Buffet with high-energy and healthy food."
    else:
        return "Custom menu for the butler."


# Example: DuckDuckGo search tool
duckduckgo_tool = DuckDuckGoSearchTool()

# Example: Visit webpage tool
visit_tool = VisitWebpageTool(max_output_length=5000)

# Example: League table tool (tool defined in a class).
league_tool = LeagueTableTool()

# Example: Importing a remote image generation tool
# image_gen_tool = load_tool("m-ric/text-to-image", trust_remote_code=True)

# Example: LangChain tools
# search_tool = Tool.from_langchain(load_tools(["serpapi"])[0])

### Agent Examples ###

def run_examples():
    # Example 1: Suggest menu
    agent_menu = CodeAgent(tools=[suggest_menu], model=model)
    print(agent_menu.run("Prepare a formal menu for the party."))

    # Example 2: DuckDuckGo search
    agent_search = CodeAgent(tools=[duckduckgo_tool], model=model)
    print(agent_search.run("Search for the best music recommendations for a Mr Robot themed party"))

    # Example 3: League table query
    agent_league = CodeAgent(tools=[league_tool], model=model)
    print(agent_league.run("How many points does Celtic football club have?"))

    # Example 4: Visit webpage
    agent_visit = ToolCallingAgent(tools=[visit_tool], model=model)
    print(agent_visit.run("Visit https://en.wikipedia.org/wiki/Celtic_F.C. and tell me when the club was founded."))

    # Example 5: Remote image generation
    # agent_image = CodeAgent(tools=[image_gen_tool], model=model, additional_authorized_imports=["PIL.Image"])
    # print(agent_image.run("Generate an image inspired by the TV show: Mr Robot"))

    # Example 6: LangChain search
    # agent_langchain = CodeAgent(tools=[search_tool], model=model)
    # print(agent_langchain.run("Search for Mr Robot themed gift ideas"))


### MAIN ###
if __name__ == "__main__":
    run_examples()