from levels import level_easy, level_medium, level_hard
from rich.panel import Panel
from rich.console import Console
console = Console()
from utils import clear, center_text, main_box, options_box
import os
import platform
if platform.system() != "Windows":
    import readline


def user_inputs():
    #formattare input dello user: al centro, maiuscolo, senza spazi iniziali e finali
    print('\n')
    text = "Digita l'opzione che preferisci per continuare: "
    centered_text = center_text(text)
    user_input = input(centered_text).upper().strip()
    return user_input


def input_asnwers(user_input):
    #risposte che user può dare, se user risponde ok si torna alla def first_slide
    if user_input in ["SKIP", "OK"]:
        return user_input
    elif user_input == "EXIT":
        console.print("\nGood bye, see you soon!\n", style= "bold magenta1", justify="center")
        exit()
    else:
        text = "uh, parola non riconosciuta 🥸   Premi invio per continuare"
        centered_text = center_text(text)
        input(centered_text)
        return user_input


def first_slide():
    #prima slide che user vede, da qui vengono richiamate le altre
    while True:
        clear()
        #box
        title = " WELCOME "
        text = "\n\n\nBentornato data-hunter! Pronto a dar la caccia ai metadati mancanti?"
        box = main_box(title, text, 100, 10)
        #opzioni
        options = ["[b][yellow]OK[/b]", "[b][yellow]SKIP[/b]", "[b][cyan1]EXIT[/b]"]
        colors = ["yellow", "yellow", "cyan1"]
        columns = options_box(options, colors)
        #print box & opzioni
        console.print(box, columns, justify="center")
        #user input
        user_input = user_inputs()
        user_input = input_asnwers(user_input)
        if user_input == "SKIP":
            break
        elif user_input == "OK":
            user_input = second_slide()
            if user_input == "SKIP":
                break
            elif user_input == "OK":
                user_input = third_slide()
                break


def second_slide():
    #opzionale seconda slide
    while True:
        clear()
        #box
        title = " INTRO "
        text = "\nIn questo workshop, avrai l'occasione di dedicarti ai metadati dei progetti sul microbioma della pelle umana provenienti da tutto il mondo! La tua partecipazione è essenziale: dovrai curare attentamente le informazioni contenute in questi metadati per garantire l'accuratezza delle analisi, delle ri-analisi e degli approcci basati sui dati che utilizzeranno queste preziose informazioni."
        box = main_box(title, text, 100, 9)
        #opzioni
        options = ["[b][yellow]OK[/b]", "[b][cyan1]SKIP[/b]", "[b][cyan1]EXIT[/b]"]
        colors = ["yellow", "cyan1", "cyan1"]
        columns = options_box(options, colors)
        #print box & opzioni
        console.print(box, columns, justify="center")
        user_input = user_inputs()
        input_asnwers(user_input)
        return user_input


def third_slide():
    #opzionale terza slide
    while True:
        clear()
        #box
        title = " INTRO "
        text = "\n\n🔍🔍🔍\nIl tuo compito sarà leggere il paper associato al progetto e prenderti cura di nove delle sue colonne. Può sembrare una piccola impresa, ma in realtà, stai contribuendo al futuro della ricerca sul microbioma della pelle umana! Coraggio! E grazie mille per il tuo contributo! :)"
        box = main_box(title, text, 100, 10)
        #opzioni
        options = ["[b][yellow]OK[/b]", "[b][cyan1]EXIT[/b]"]
        colors = ["yellow", "cyan1"]
        columns = options_box(options, colors)
        #print box & opzioni
        console.print(box, columns, justify="center")
        user_input = user_inputs()
        input_asnwers(user_input)
        return user_input


def username():
    #ricava username, che è uguale al nome della cartella contenente i progetti da curare
    while True:
        clear()
        text = "Digita il tuo username: "
        centered_text = center_text(text)
        user_name = input(centered_text).lower().strip()
        participants = ["acerbis", "bacchi", "barillari", "benocci", "bovolini", "cammarano", "capuano", "carbutti", "cattaneo", "chaji", "cirimpei", "cividini", "colleoni", "colombo", "diamanti", "huaman", "ierano", "impieri", "lazzari", "marin", "meziu", "minotti", "pellin", "pertesana", "piva", "riva", "santambrogio", "villa", "volonterio", "fumagalli"]
        if user_name != "" and user_name in participants:
            return user_name
        else:
            console.print(f'\nNon trovo nessun "{user_name}" nel mio registro di data-hunters 💀  Inseririsci lo username che ti è stato comunicato a lezione!', justify="center")
            text = "Premi invio per continuare "
            centered_text = center_text(text)
            input(centered_text)


def project_selection(user_input):
    #selezione del progetto da curare
    while True:
        clear()
        participants_prjs_dict = {'acerbis': ['DRP000933', 'DRP003134', 'DRP003136', 'DRP003368', 'DRP003546', 'DRP004280', 'DRP004449', 'DRP005567', 'DRP005568', 'DRP005871', 'DRP007889', 'DRP008069', 'DRP008559', 'SRP462919'], 'bacchi': ['DRP009543', 'DRP009553', 'ERP000071', 'ERP001059', 'ERP002478', 'ERP004469', 'ERP005135', 'ERP005151', 'ERP005152', 'ERP005182', 'ERP005296', 'ERP005633', 'ERP005635', 'SRP467783'], 'barillari': ['ERP005806', 'ERP006039', 'ERP008469', 'ERP008694', 'ERP008799', 'ERP010075', 'ERP012216', 'ERP012803', 'ERP012810', 'ERP012879', 'ERP012880', 'ERP013063', 'ERP014521'], 'benocci': ['ERP014863', 'ERP016116', 'ERP016280', 'ERP016491', 'ERP016629', 'ERP016977', 'ERP017003', 'ERP018577', 'ERP019566', 'ERP020615', 'ERP020884', 'ERP020891', 'ERP020892'], 'bovolini': ['ERP021491', 'ERP021574', 'ERP021896', 'ERP022166', 'ERP022226', 'ERP022626', 'ERP022657', 'ERP023327', 'ERP103940', 'ERP104625', 'ERP104834', 'ERP105323', 'ERP106593'], 'cammarano': ['ERP107881', 'ERP108717', 'ERP109059', 'ERP109379', 'ERP109520', 'ERP109605', 'ERP110254', 'ERP110351', 'ERP110833', 'ERP111616', 'ERP112507', 'ERP113722', 'ERP113817'], 'capuano': ['ERP114401', 'ERP115175', 'ERP115350', 'ERP115809', 'ERP116867', 'ERP118380', 'ERP120065', 'ERP120105', 'ERP120109', 'ERP120993', 'ERP122936', 'ERP122952', 'ERP123154'], 'carbutti': ['ERP123984', 'ERP124074', 'ERP124721', 'ERP125421', 'ERP125422', 'ERP125919', 'ERP126104', 'ERP127805', 'ERP128242', 'ERP128881', 'ERP129151', 'ERP129222', 'ERP130862'], 'cattaneo': ['ERP131433', 'ERP133893', 'ERP138010', 'ERP143983', 'ERP148295', 'ERP148522', 'SRP000393', 'SRP000487', 'SRP000574', 'SRP000642', 'SRP000689', 'SRP002096', 'SRP002421'], 'chaji': ['SRP002480', 'SRP004700', 'SRP004724', 'SRP005016', 'SRP005019', 'SRP005031', 'SRP005032', 'SRP005033', 'SRP005034', 'SRP005035', 'SRP005036', 'SRP005037', 'SRP005038'], 'cirimpei': ['SRP005039', 'SRP005040', 'SRP005041', 'SRP005042', 'SRP005043', 'SRP005044', 'SRP005045', 'SRP005046', 'SRP005047', 'SRP005048', 'SRP005049', 'SRP005050', 'SRP005051'], 'cividini': ['SRP005052', 'SRP005053', 'SRP005054', 'SRP005055', 'SRP005056', 'SRP005057', 'SRP005059', 'SRP005060', 'SRP005061', 'SRP005062', 'SRP005063', 'SRP005064', 'SRP005065'], 'colleoni': ['SRP005066', 'SRP005067', 'SRP005068', 'SRP005069', 'SRP005070', 'SRP005071', 'SRP005072', 'SRP005073', 'SRP005074', 'SRP005075', 'SRP005076', 'SRP005077', 'SRP005078'], 'colombo': ['SRP005079', 'SRP005080', 'SRP005081', 'SRP005082', 'SRP005083', 'SRP005084', 'SRP005085', 'SRP005086', 'SRP005087', 'SRP005088', 'SRP005089', 'SRP005090', 'SRP005091'], 'diamanti': ['SRP009573', 'SRP015995', 'SRP044386', 'SRP046302', 'SRP049645', 'SRP050070', 'SRP050097', 'SRP051059', 'SRP051251', 'SRP056364', 'SRP056554', 'SRP056821', 'SRP057467'], 'huaman': ['SRP057641', 'SRP057859', 'SRP059432', 'SRP059484', 'SRP059791', 'SRP062726', 'SRP065088', 'SRP067274', 'SRP067489', 'SRP071579', 'SRP071608', 'SRP074170', 'SRP076355'], 'ierano': ['SRP076549', 'SRP076583', 'SRP077514', 'SRP078001', 'SRP080294', 'SRP080713', 'SRP090974', 'SRP091027', 'SRP091029', 'SRP099070', 'SRP100204', 'SRP100409', 'SRP104271'], 'impieri': ['SRP109004', 'SRP109057', 'SRP111440', 'SRP113602', 'SRP113697', 'SRP115298', 'SRP115591', 'SRP116098', 'SRP117096', 'SRP126376', 'SRP128102', 'SRP135834', 'SRP135853'], 'lazzari': ['SRP144396', 'SRP148521', 'SRP155952', 'SRP159209', 'SRP160100', 'SRP162849', 'SRP164182', 'SRP165966', 'SRP167860', 'SRP170931', 'SRP178530', 'SRP179702', 'SRP182987'], 'marin': ['SRP185615', 'SRP185750', 'SRP186628', 'SRP187334', 'SRP198954', 'SRP213896', 'SRP214169', 'SRP218078', 'SRP218925', 'SRP223693', 'SRP226826', 'SRP241991', 'SRP246147'], 'meziu': ['SRP247203', 'SRP247381', 'SRP249658', 'SRP251660', 'SRP252817', 'SRP254073', 'SRP254079', 'SRP255681', 'SRP258297', 'SRP258303', 'SRP259267', 'SRP259700', 'SRP260397'], 'minotti': ['SRP262012', 'SRP265017', 'SRP267233', 'SRP267292', 'SRP268790', 'SRP270928', 'SRP271795', 'SRP274219', 'SRP275714', 'SRP276001', 'SRP276976', 'SRP277503', 'SRP282499'], 'pellin': ['SRP284376', 'SRP284481', 'SRP285536', 'SRP287343', 'SRP290878', 'SRP290885', 'SRP291174', 'SRP293771', 'SRP296983', 'SRP298493', 'SRP299034', 'SRP299855', 'SRP300200'], 'pertesana': ['SRP301556', 'SRP301876', 'SRP301881', 'SRP302424', 'SRP307213', 'SRP308225', 'SRP308666', 'SRP315427', 'SRP316179', 'SRP322848', 'SRP323315', 'SRP323470', 'SRP324179'], 'piva': ['SRP324647', 'SRP325397', 'SRP326529', 'SRP329054', 'SRP329173', 'SRP330206', 'SRP332442', 'SRP332768', 'SRP333994', 'SRP334017', 'SRP335200', 'SRP335939', 'SRP337076'], 'riva': ['SRP337963', 'SRP339189', 'SRP339672', 'SRP341645', 'SRP350368', 'SRP350643', 'SRP351228', 'SRP352096', 'SRP353911', 'SRP354785', 'SRP358030', 'SRP358974', 'SRP361274'], 'santambrogio': ['SRP361438', 'SRP363461', 'SRP364419', 'SRP367000', 'SRP375515', 'SRP377367', 'SRP378150', 'SRP378874', 'SRP379026', 'SRP379413', 'SRP380137', 'SRP380142', 'SRP381964'], 'villa': ['SRP384954', 'SRP385168', 'SRP388128', 'SRP389252', 'SRP393003', 'SRP396034', 'SRP402528', 'SRP403403', 'SRP404611', 'SRP404690', 'SRP409258', 'SRP410442', 'SRP416140'], 'volonterio': ['SRP416437', 'SRP417930', 'SRP418159', 'SRP418687', 'SRP423944', 'SRP426277', 'SRP428383', 'SRP434329', 'SRP434527', 'SRP441930', 'SRP450914', 'SRP454607', 'SRP459340']}
        console.print("\n\nEcco i progetti che ti aspettano. È il momento di scegliere il tuo destino: seleziona il progetto che diventerà la tua avventura di oggi ⚔️", justify="center")
        print("\n")
        for prj in participants_prjs_dict[user_name]:
            console.print(f"""[bold yellow]{prj}""", justify="center")
        print("\n")
        text = "Digita il nome del file: "
        centered_text = center_text(text)
        user_input_file = input(centered_text).upper().strip()
        if user_input_file in participants_prjs_dict[user_name]:
            return user_input_file
        else:
            console.print(f'\nNon trovo nessun "{user_input_file}" nella lista di progetti che devi curare...' , justify="center")
            text = "Premi invio per continuare "
            centered_text = center_text(text)
            input(centered_text)




def menu_levels(user_name, project):
    #menù principale in cui lo user sceglie il livello di difficoltà con cui vuole affrontare la manual curation
    while True:
        clear()
        easy_box = Panel("\n\nEASY ★", style="bold magenta1", border_style="magenta1", padding=(1, 1), width=75, height=8)
        medium_box = Panel("\n\nMEDIUM ★ ★", style="bold magenta1", border_style="magenta1", padding=(1, 1), width=75, height=8)
        hard_box = Panel("\n\nHARD ★ ★ ★", style="bold magenta1", border_style="magenta1", padding=(1, 1), width=75, height=8)
        console.print(easy_box, medium_box, hard_box, justify="center")

        options = ["[b][cyan1]BACK[/b]", "[b][cyan1]EXIT[/b]"]
        colors = ["cyan1", "cyan1"]
        columns = options_box(options, colors)
        console.print(columns, justify="center")
    
        text = "Con quale livello di difficoltà vuoi sfidarti oggi? Digita la tua scelta: "
        centered_text = center_text(text)
        print("\n")
        user_input = input(centered_text).upper().strip()
        if user_input == "EASY":
            level_easy(project)
            continue
        elif user_input == "MEDIUM":
            level_medium(project)
            continue
        elif user_input == "HARD":
            level_hard(project)
            continue
        elif user_input == "BACK":
            project_selection(user_name)
        elif user_input == "EXIT":
            console.print("\nGood bye, see you soon!\n", style= "bold magenta1", justify="center")
            exit()
        else:
            text = "Livello non valido 🌵   Riprova!"
            centered_text = center_text(text)
            input(centered_text)


if __name__ == "__main__":
    while True:
        #main_logo()
        if platform.system() != "Windows":
            readline.parse_and_bind('tab: complete')
            readline.set_completer_delims(' \t\n')
        first_slide()
        user_name = username()
        project = project_selection(user_name)
        menu_levels(user_name, project)