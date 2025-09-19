# Unit 2.1 The smolagents framework
from smolagents import (CodeAgent, DuckDuckGoSearchTool, InferenceClientModel, tool, Tool, VisitWebpageTool,
                        FinalAnswerTool, ToolCallingAgent, LiteLLMModel, load_tool)
from langfuse import get_client
from openinference.instrumentation.smolagents import SmolagentsInstrumentor
from tools import league_table_tool
from tools.league_table_tool import LeagueTableTool
from PIL import Image
from langchain_community.agent_toolkits.load_tools import load_tools

# Langfuse Telemetry
langfuse = get_client()
if langfuse.auth_check():
    print("Langfuse client is authenticated and ready!")
else:
    print("Authentication failed. Please check your credentials and host.")

SmolagentsInstrumentor().instrument()

# Local model
model = LiteLLMModel(
    model_id="ollama_chat/qwen2:7b",
    api_base="http://127.0.0.1:11434",
    num_ctx=8192,
)


# Finding a party playlist using DuckDuckGo
# agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)
# agent.run("Search for the best music recommendations for a Mr Robot themed party")

# Suggest menu based on the occasion

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


# agent = CodeAgent(tools=[suggest_menu], model=model)
# agent.run("Prepare a formal menu for the party.")


# agent = CodeAgent(tools=[], model=InferenceClientModel(), additional_authorized_imports=['datetime'])

# Preparing the menu for the party
# agent.run("Prepare a formal menu for the party.")

# Work out party preparation time
# agent.run(
#     """
#     Alfred needs to prepare for the party. Here are the tasks:
#     1. Prepare the drinks - 30 minutes
#     2. Decorate the mansion - 60 minutes
#     3. Set up the menu - 45 minutes
#     4. Prepare the music and playlist - 45 minutes
#
#     If we start right now, at what time will the party be ready?
#     """
# )

# Using a ToolCallingAgent (generates JSON to call tools)
# agent = ToolCallingAgent(tools=[DuckDuckGoSearchTool()], model=model)
# agent.run("What was the score in the last game of football played by Celtic Football Club?")

# Using a tool defined in a class
# agent = CodeAgent(tools=[LeagueTableTool()], model=model)
# agent.run("How many points does Celtic football club have?")

# Using built-in tools
# visit_tool = VisitWebpageTool(max_output_length=5000)
# agent = ToolCallingAgent(tools=[visit_tool], model=model)
# result = agent.run("Visit https://en.wikipedia.org/wiki/Celtic_F.C. and tell me when the club was founded.")

# Import tool from Hub
# image_gen_tool = load_tool("m-ric/text-to-image", trust_remote_code=True)
# agent = CodeAgent(tools=[image_gen_tool],model=model, additional_authorized_imports=["PIL.Image"])
# result = agent.run("Generate an image inspired by the TV show: Mr Robot")

# Using a LangChain tool
# search_tool = Tool.from_langchain(load_tools(["serpapi"])[0])
# agent = CodeAgent(tools=[search_tool], model=model)
# agent.run("Search for Mr Robot themed gift ideas")