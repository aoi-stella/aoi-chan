from bot.bot_controller import BotController
from utils.env import DotEnvLoader

bot_controller: BotController = None

def __instance_init():
    global bot_controller
    
    DotEnvLoader.load_env("./.env")
    bot_controller = BotController()
    return

def __main():
    global bot_controller
    
    __instance_init()
    bot_controller.run_bot()
    return

if __name__ == "__main__":
    __main()