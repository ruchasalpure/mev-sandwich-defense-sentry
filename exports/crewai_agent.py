from crewai import Agent

mev_sandwich_defense_sentry = Agent(
    role="Mev Sandwich Defense Sentry",
    goal="Deliver high-precision autonomous Mev Sandwich Defense Sentry operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
