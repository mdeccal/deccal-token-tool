
from Helper import *
from Helper.Common.utils import *

clear()

color = Fore.GREEN

def change_theme():
    global color
    clear()
    print_banner(color)
    print(f"""
{color}<<{Fore.RESET}1{color}>>  [{Fore.RESET}Light Magenta (Standart){color}]
{color}<<{Fore.RESET}2{color}>>  [{Fore.RESET}Light Blue{color}]
{color}<<{Fore.RESET}3{color}>>  [{Fore.RESET}Light Red{color}]
{color}<<{Fore.RESET}4{color}>>  [{Fore.RESET}Light Green{color}]
{color}<<{Fore.RESET}5{color}>>  [{Fore.RESET}Light Cyan{color}]
{color}<<{Fore.RESET}6{color}>>  [{Fore.RESET}Light Yellow{color}]
{color}<<{Fore.RESET}7{color}>>  [{Fore.RESET}Magenta{color}]
{color}<<{Fore.RESET}8{color}>>  [{Fore.RESET}Blue{color}] 
{color}<<{Fore.RESET}9{color}>>  [{Fore.RESET}Red{color}]
{color}<<{Fore.RESET}10{color}>> [{Fore.RESET}Green{color}]
{color}<<{Fore.RESET}11{color}>> [{Fore.RESET}Cyan{color}]
{color}<<{Fore.RESET}12{color}>> [{Fore.RESET}Yellow{color}]
    """)
    choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Seçenek: ")
    colors = {
        "1": Fore.LIGHTMAGENTA_EX,
        "2": Fore.LIGHTBLUE_EX,
        "3": Fore.LIGHTRED_EX,
        "4": Fore.LIGHTGREEN_EX,
        "5": Fore.LIGHTCYAN_EX,
        "6": Fore.LIGHTYELLOW_EX,
        "7": Fore.MAGENTA,
        "8": Fore.BLUE,
        "9": Fore.RED,
        "10": Fore.GREEN,
        "11": Fore.CYAN,
        "12": Fore.YELLOW
    }
    color = colors.get(choice)
    if color:
        color = color
    else:
        print("Yanlış seçenek")
        time.sleep(1)

def main():
    new_title("mdeccal Token Tool │ Sayfa 1")
    clear()
    print_banner(color)
    print(f"""
                    {color}<<{Fore.RESET}1{color}>> [{Fore.RESET}Token Formater{color}]        {color}<<{Fore.RESET}8{color}>>  [{Fore.RESET}Proxy Scraper{color}]         {color}<<{Fore.RESET}15{color}>>  [{Fore.RESET}Token Mail verifier{color}]
                    {color}<<{Fore.RESET}2{color}>> [{Fore.RESET}Token Checker{color}]         {color}<<{Fore.RESET}9{color}>>  [{Fore.RESET}Proxy Checker{color}]         {color}<<{Fore.RESET}16{color}>>  [{Fore.RESET}Token Pass Changer{color}]
                    {color}<<{Fore.RESET}3{color}>> [{Fore.RESET}Token Sorter{color}]          {color}<<{Fore.RESET}10{color}>> [{Fore.RESET}Webhook Tool{color}]          {color}<<{Fore.RESET}17{color}>>  [{Fore.RESET}Token Onliner{color}]
                    {color}<<{Fore.RESET}4{color}>> [{Fore.RESET}Token spammer{color}]         {color}<<{Fore.RESET}11{color}>> [{Fore.RESET}Faker Tool{color}]            {color}<<{Fore.RESET}18{color}>>  [{Fore.RESET}Token Status Rotator{color}]
                    {color}<<{Fore.RESET}5{color}>> [{Fore.RESET}Token Guild Checker{color}]   {color}<<{Fore.RESET}12{color}>> [{Fore.RESET}Token Nuker{color}]           {color}<<{Fore.RESET}19{color}>>  [{Fore.RESET}Token Editor{color}]
                    {color}<<{Fore.RESET}6{color}>> [{Fore.RESET}Token Guild Leaver{color}]    {color}<<{Fore.RESET}13{color}>> [{Fore.RESET}Clear Output Folder{color}]   {color}<<{Fore.RESET}20{color}>>  [{Fore.RESET}Discord Nuker{color}] 
                    {color}<<{Fore.RESET}7{color}>> [{Fore.RESET}Clear Input Folder{color}]    {color}<<{Fore.RESET}14{color}>> [{Fore.RESET}Nitro Gift Checker{color}]    {color}<<{Fore.RESET}21{color}>>  [{Fore.RESET}Get Own Token{color}] 
    """)
    choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Seçenek: ")
    functions = {
        "1": formater,
        "2": Token_checker,
        "3": sort_tokens,
        "4": token_spammer,
        "5": check_tokens_guild,
        "6": token_leave_server,
        "7": clear_input,
        "8": Proxy_scraper,
        "9": check_proxys,
        "10": Webhook_tool,
        "11": main_faker,
        "12": Token_nuker,
        "13": clear_output,
        "14": check_codes,
        "15": TokenMailverifier,
        "16": pass_changer,
        "17": online_tokens,
        "18": status_changer,
        "19": token_editor,
        "20": Discord_nuker,
        "21": get_own_token,
        "x2": main2,
        "x3": social_menu
    }
    function = functions.get(choice)
    if function:
        function()
    else:
        print("Yanlış seçenek")
        time.sleep(1)
    main()

def main2():
    new_title("mdeccal Token Tool │ Sayfa 2")
    clear()
    print_banner(color)
    print(f"""                        
                    {color}<<{Fore.RESET}22{color}>> [{Fore.RESET}Token Login{color}]              
                    {color}<<{Fore.RESET}23{color}>> [{Fore.RESET}Token Leave Groups{color}]
                    {color}<<{Fore.RESET}24{color}>> [{Fore.RESET}Gen Test Token{color}]
                    {color}<<{Fore.RESET}25{color}>> [{Fore.RESET}Get Token Info{color}]      
                    {color}<<{Fore.RESET}26{color}>> [{Fore.RESET}Id To Token{color}]                 
    """)
    choice = input(f"{Fore.RESET}[{color}>{Fore.RESET}] Seçenek: ")
    functions = {
       
       
        "22": token_login,
        "23": token_leave_server,
        "24": gen_token,
        "25": fetch_user_details,
        "26": id__token,
        "x1": main,
        "x3": social_menu
    }
    function = functions.get(choice)
    if function:
        function()
    else:
        print("invalid choice")
        time.sleep(1)
    main2()

StartupTool()
os.system("mode con cols=135 lines=24")
main()