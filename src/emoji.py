import os
import openai

EXAMPLES = {
    ":tada:": "initial commit",
    ":sparkles:": "when adding a new user-facing feature",
    ":art:": "when improving UI",
    ":package:": "when refactoring or improving code",
    ":racehorse:": "when improving performance",
    ":lock:": "when improving security",
    ":wrench:": "when updating configs",
    ":wheelchair:": "when improving accessibility",
    ":rocket:": "when improving dev tools",
    ":pencil:": "when writing docs (e.g. README)",
    ":gem:": "when cutting a new release / version bump",
    ":bug:": "when fixing a bug",
    ":boom:": "when fixing a crash",
    ":non-potable_water:": "when fixing a memory leak",
    ":fire:": "when removing code or files",
    ":white_check_mark:": "when adding new tests",
    ":green_heart:": "when fixing the CI build",
    ":shirt:": "when fixing linter warnings",
    ":satellite:": "when adding instrumentation or metrics",
    ":loud_sound:": "when adding logging",
    ":mute:": "when removing logging",
    ":arrow_up:": "when upgrading dependencies",
    ":arrow_down:": "when downgrading dependencies",
    ":crossed_flags:": "when adding an A/B test or feature flag**",
    ":zap:": "when making a backwards-incompatible change**",
    ":construction:": "when the change is a work in progress (do not merge)**",
}


class Bot:
    def __init__(self):
        openai.api_key = os.environ.get("OPENAI_API_KEY")

    def create_prompt(self, message: str):
        base_prompt = f""" 
        Adding one emoji at the start of a commit message makes them cooler and cleaner.
        i will write a commit message and you have to add an emoji on start according to 
        following {EXAMPLES}. You only have to add an emoji at start that best suits and 
        response should only be update message. You can also capitalize some words if need.
        Nothing else should be provided in response,whatsoever. User: """
        return f'{base_prompt} {message} Chat:'
    
    def get_response(self, message: str):
        response = openai.Completion.create(
            engine="text-chat-davinci-002-20221122",
            prompt=self.create_prompt(message),
            temperature=0.6,
            max_tokens=800,
            stop=["\n\n\n"]
        )
        return response["choices"][0]["text"].strip().removesuffix("<|im_end|>")


def main():
    bot = Bot()
    print(bot.get_response("initial commit"))
    
    
main()