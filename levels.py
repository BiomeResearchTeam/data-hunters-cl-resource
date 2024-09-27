from rich.text import Text
from rich.panel import Panel
from rich.columns import Columns
from rich.console import Console
console = Console()
from utils import clear, center_text, main_box, options_box
import os


def curation_function(title, text_main, text_hint, text_solution, main_height, sol_height):
    #funzione generica che ha un box che contiene il testo e 3 opzioni. i testi delle 3 funzioni sono dati come argomento
    while True:
        clear()
        box = main_box(title, text_main, 100, main_height)
        #opzioni
        options = ["[b][yellow]OK[/b]", "[b][cyan1]HINT[/b]", "[b][cyan1]SOLUTION[/b]"]
        colors = ["yellow", "cyan1", "cyan1"]
        columns = options_box(options, colors)
        #print box & opzioni
        console.print(box, columns, justify="center")
        #user input
        text = "Digita l'opzione che preferisci per continuare:  "
        centered_text = center_text(text)
        print("\n")
        user_input = input(centered_text).upper().strip()
        #input_asnwers(user_input)
        if user_input == "OK":
            return
        elif user_input == "HINT":
            clear()
            title = " HINT "
            box = main_box(title, text_hint, 100, 13)
            options = ["[b][yellow]OK[/b]"]
            colors = ["yellow"]
            columns = options_box(options, colors)
            console.print(box, columns, justify="center")
            text = "Premi invio per continuare "
            centered_text = center_text(text)
            input(centered_text)
        elif user_input == "SOLUTION":
            clear()
            title = " SOLUTION "
            text_title = Text.assemble(title)
            text_content = Text.assemble(text_solution, style=None, justify="left")
            box = Panel(text_content, title=text_title, border_style="magenta1", padding=(0, 1), width=105, height=sol_height)
            options = ["[b][yellow]OK[/b]"]
            colors = ["yellow"]
            columns = options_box(options, colors)
            console.print(box, columns, justify="center")
            text = "Premi invio per continuare "
            centered_text = center_text(text)
            input(centered_text)
            return


def level_easy(project):
    while True:
        clear()
        #presentazione delle 9 opzioni di steps da fare nella manual curation
        project_file = os.path.splitext(os.path.basename(project))[0].replace(".tsv", "")
        intro_box = Panel(f"\n{project_file}", title=" SELECTED PROJECT ", style="bold", border_style="magenta1", padding=(0, 1), width=50, height=5)
        console.print(intro_box, justify="center")
        print("\n")
        options = ["[b][yellow]1. DEEPNOTE[/b]", "[b][yellow]2. IMPORT LIBRARY[/b]", "[b][yellow]3. READ DATAFRAME[/b]"]
        colors = ["yellow", "yellow", "yellow"]
        choice = [Panel(opt.center(45), border_style=color, padding=(1, 1), width=40) for opt, color in zip(options, colors)]
        console.print(Columns(choice), justify="center")
        options = ["[b][yellow]4. EXTRACT DOI[/b]", "[b][yellow]5. PROJECT SUITABILITY[/b]", "[b][yellow]6. ADD NEW COLUMNS[/b]"]
        choice = [Panel(opt.center(45), border_style=color, padding=(1, 1), width=40) for opt, color in zip(options, colors)]
        console.print(Columns(choice), justify="center")
        options = ["[b][yellow]7. SAVE FILE[/b]"]
        choice = [Panel(opt.center(45), border_style=color, padding=(1, 1), width=40) for opt, color in zip(options, colors)]
        console.print(Columns(choice), justify="center")

        options = ["[b][cyan1]BACK[/b]", "[b][cyan1]EXIT[/b]"]
        colors = ["cyan1", "cyan1"]
        columns = options_box(options, colors)
        console.print(columns, justify="center")
        
        #scelta dello step di manual curation da fare
        text = "Quale step devi affrontare? Digita il numero corrispondente: "
        centered_text = center_text(text)
        print("\n")
        user_input = input(centered_text).upper().strip()
        options_dict = {
        "1": (f" {project} - DEEPNOTE ", "\n\n\n\nPer iniziare, apri un nuovo Notebook cliccando sul +", "\n\n\n\n\nIn alto a sinistra vedi dove c'è scritto 'Notebooks'? Clicca sul +", "\n\n\n\nDai crediamo in te! 🫶", 10, 11),
        "2": (f" {project} - PANDAS ", "\n\n\n\nImporta la libreria pandas!", "\n\n\n\n\nPer usare una libreria in python bisogna prima importarla...", "\n\n\n\nimport pandas as pd", 10, 11),
        "3": (f" {project} - DATAFRAME ", "\n\n\n\nLeggi il file come dataframe di pandas!", "\n\n\n\nPer leggere il file usa la libreria pandas... e non dimenticarti del separatore con cui è formattato il file!",  f'\n\n\n\ndf = pd.read_csv("{project}_df.tsv", sep="\\t")', 10, 11),
        "4": (f" {project} - EXTRACT DOI ", '\n\n\nEstrai dal dataframe il DOI con cui potrai leggere la pubblicazione scientifica! La colonna che contiene questa informazione si chiama "DOI"', "\n\n\n\nPrima seleziona solo la colonna che ti interessa dal dataframe... e poi prendi solo i valori unici della colonna!", '\n\n\n\ndoi = df["DOI"].unique()', 10, 11),
        "5": (f" {project} - SUITABILITY ", '\nLeggi la pubblicazione! Innanzitutto: è un progetto di metagenomica? E inoltre, in questo progetto è stato campionato il microbioma della pelle di uomo? \n\n✅ Se ad entrambe le domande hai risposto "sì", procedi a fare il prossimo step.\n\n❌ Altrimenti, se anche solo una delle due domande ha come risposta "no", segna questo progetto nel tuo report, contattaci su Classroom, e inizia pure a lavorare su un altro progetto!',\
              '\n\n🧬🧬🧬 Per capire se è un progetto è di metagenomica è utile chiedersi: "è stato campionato il microbioma? è stato sequenziato il DNA dei campioni raccolti? viene citato l approccio AMPLICON o WGS?"\n\n✌️  ✌️  ✌️  Per capire se è stato campionato il microbioma della pelle di uomo puoi guardare nei Materiali e Metodi se i soggetti dello studio sono uomini e hanno campionato siti della loro pelle!', \
                 "\n\n\n\nNon c'è una soluzione fissa in questo step, questa sfida è completamente nelle tue mani! 💫🪄", 12, 11),
        "6": (f" {project} - NEW COLUMNS ", '\n\nEhi Data Hunter, sei arrivato allo step più critico: curare il contenuto del dataframe di metadati. Niente paura, ti spieghiamo tutto. Ti ricordiamo che le colonne da curare sono 9: \
              \n\n1) "library_strategy": la strategia di sequenziamento (AMPLICON, WGS)\n\n2) "instrument_platform": la piattaforma di sequenziamento (ILLUMINA, ION TORRENT, ...)\n\n3) "instrument_model": modello di sequenziatore (ILLUMINA MiSeq, ILLUMINA NovaSeq, ...)\
              \n\n4) "SKIOME_amplicon_target": amplicone targettato (16S, ITS, ...)\n\n5) "SKIOME_target_region": regione ipervariabile dell amplicone (V1, V3-V4, ...)\n\n6) "SKIOME_primer": primer (GTGCCAGCMGCCGCGGTAA, GGACTACNVGGGTWTCTAAT, ...)\
              \n\n7) "SKIOME_individuals_nationality": nazionalità degli individui campionati (Italy, Spain, ...)\n\n8) "SKIOME_body_site": sito del corpo campionato (hands, forehead, ...)\n\n9) "SKIOME_status": condizione o stato che si attribuisce ai soggetti campionati in base alle diverse ipotesi considerate (healthy vs disease, rural vs urban, ...) \
              \n\n\n1️⃣  Le colonne "library_strategy", "instrument_platform", "instrument_model" sono già presenti nel tuo dataframe! Controlla che l informazione che hai trovato nella pubblicazione sia uguale a quella presente nel dataframe \
              \n2️⃣  Tutte le altre colonne potrebbero esserci nel tuo dataframe ma non con certezza: devi cercarle! 🅰️  Per le colonne che esistono fai come nel punto 1: controlla che l informazione che hai trovato nella pubblicazione sia uguale a quella presente nel dataframe. 🅱️  Per le colonne che non esistono: devi crearle e compilarle con l informazione trovata!\
              \n\n\n⚠️  Se trovi che in una colonna dovrebbe essere contenuto più di un valore, per esempio hanno campionato il microbioma della pelle delle mani e del viso contattaci su Classroom e ti diremo come agire!\n⚠️  In ogni caso, se hai dubbi sul valore da compilare contattaci su Classroom!\
              \n\n\n💎 Questo è lo step più prezioso: ricercatori di tutto il mondo scaricheranno i progetti che hai curato, e daranno per scontato che le informazioni siano impeccabili. Il futuro della ricerca del microbioma della pelle di uomo è anche nelle (e sulle eheh) tue mani.', \
              '\n1️⃣  Per le colonne che già esistono, estrai la colonna dal dataframe (PS il nome della colonna è proprio come l abbiamo chiamata nel box principale!🧠 )... e poi seleziona solo i valori unici! \
                \n\n2️⃣  Per le colonne da cercare, usa l informazione che hai trovato nella pubblicazione come valore da trovare nelle varie colonne del dataframe! \
                \n🅰️  Se la colonna esiste, estrai la colonna dal dataframe e poi seleziona solo i valori unici! Verifica se il valore che hai trovato nella pubblicazione è uguale a quello presente nel df: se è diverso crea una nuova colonna! \
                \n🅱️  Se la colonna non esiste, crea una nuova colonna e associa il valore che hai trovato nella pubblicazione',\
                '\n\n1️⃣\nvalori = df["nome_della_colonna"].unique()\nprint(valori)\
                \n\n\n2️⃣\ncolonne = df.columns.to_list()\ncolonne_trovate=[]\n\n>>>SPIEGAZIONE: prima crea una lista delle colonne del tuo df, e poi crea una lista vuota che si riempirà delle colonne del df in cui è stato trovato il valore\
                \n\nfor colonna in colonne:\n   if "valore".lower() in colonna.lower():\n      colonne_trovate.append(colonna)\
                \n   else:\n      pass\n\n>>>SPIEGAZIONE: per ciascuna colonna presente nella lista colonne, cerca se il valore della pubblicazione è presente nella colonna. se è presente allora segna il nome della colonna in cui è stato trovato nella lista colonne_trovate. Se non è presente in quella colonna il loop continua senza segnare nulla\
                \n\n🅰️  if len(colonne_trovate)>0:\n      for colonna in colonne_trovate:\n         print(df[colonna].unique())\
                \n   else:\n      print("nessuna colonna trovata!")\n\n🅱️  df["SKIOME_nome_della_colonna"] = "valore trovato nel paper")\n\n>>>SPIEGAZIONE: se la lunghezza della lista colonne_trovate è maggiore di 0 significa che nel tuo dataframe esiste almeno una colonna contenente il valore che hai trovato nella pubblicazione. Stampa i valori contenuti in ciascuna delle colonne presenti nella lista colonne_trovate per verificare se il valore contenuto in questa/e colonna/e è lo stesso. Se non è uguale, crea una nuova colonna con il valore corretto!\
                \nInvece, se non hai trovato il valore nel dataframe, significa che nel dataframe non esiste una colonna specifica che contiene quel valore. Quindi crea una nuova colonna e riempila con il valore che hai trovato nel paper', 45, 45),
        "7": (f" {project} - SAVING FILE ", f'\n\nOra che il dataframe dei metadati è stato curato alla perfezione, è tempo di salvarlo sotto forma di file TSV!\n\nIl nome del file da salvare deve essere: "SKIOME_{project}_df.tsv"', "\n\n\nIndica il dataframe, il nome del file che vuoi salvare e il separatore delle righe!", f'\n\n\ndf.to_csv("SKIOME_{project}_df.tsv", sep="\\t", index=False)', 10, 11)
        }

        if user_input in options_dict:
            arguments = options_dict[user_input]
            curation_function(*arguments)
        elif user_input == "BACK":
            return
        elif user_input == "EXIT":
            console.print("\nGood bye, see you soon!\n", style= "bold magenta1", justify="center")
            exit()
        else:
            text = "Risposta non valida 🪇   Sei sicuro di aver digitato un numero da 1 a 7?"
            centered_text = center_text(text)
            input(centered_text)


#da scrivere i testi dei box, cioè decidere gli step curation da far fare che siano medium                                         
def level_medium(project):
    while True:
        clear()
        #presentazione delle 9 opzioni di steps da fare nella manual curation
        project_file = os.path.splitext(os.path.basename(project))[0].replace(".tsv", "")
        intro_box = Panel(f"\n{project_file}", title=" SELECTED PROJECT ", style="bold", border_style="magenta1", padding=(0, 1), width=50, height=5)
        console.print(intro_box, justify="center")
        print("\n")
        options = ["[b][yellow]1. DEEPNOTE[/b]", "[b][yellow]2. IMPORT LIBRARY[/b]", "[b][yellow]3. READ DATAFRAME[/b]"]
        colors = ["yellow", "yellow", "yellow"]
        choice = [Panel(opt.center(45), border_style=color, padding=(1, 1), width=40) for opt, color in zip(options, colors)]
        console.print(Columns(choice), justify="center")
        options = ["[b][yellow]★ 4. EXTRACT DOI[/b]★ ", "[b][yellow]5. PROJECT SUITABILITY[/b]", "[b][yellow]★ 6. ADD NEW COLUMNS ★[/b]"]
        choice = [Panel(opt.center(45), border_style=color, padding=(1, 1), width=40) for opt, color in zip(options, colors)]
        console.print(Columns(choice), justify="center")
        options = ["[b][yellow]7. SAVE FILE[/b]"]
        choice = [Panel(opt.center(45), border_style=color, padding=(1, 1), width=40) for opt, color in zip(options, colors)]
        console.print(Columns(choice), justify="center")

        options = ["[b][cyan1]BACK[/b]", "[b][cyan1]EXIT[/b]"]
        colors = ["cyan1", "cyan1"]
        columns = options_box(options, colors)
        console.print(columns, justify="center")
        
        #scelta dello step di manual curation da fare
        text = "Quale step devi affrontare? Gli step con le stelle sono quelli dove la difficolta ora è maggiore! Digita il numero corrispondente: "
        centered_text = center_text(text)
        print("\n")
        user_input = input(centered_text).upper().strip()


        options_dict = {
        "1": (f" {project} - DEEPNOTE ", "\n\n\n\nPer iniziare, apri un nuovo Notebook cliccando sul +", "\n\n\n\n\nIn alto a sinistra vedi dove c'è scritto 'Notebooks'? Clicca sul +", "\n\n\n\nDai crediamo in te! 🫶", 10, 11),
        "2": (f" {project} - PANDAS ", "\n\n\n\nImporta la libreria pandas!", "\n\n\n\n\nPer usare una libreria in python bisogna prima importarla...", "\n\n\n\nimport pandas as pd", 10, 11),
        "3": (f" {project} - DATAFRAME ", "\n\n\n\nLeggi il file come dataframe di pandas!", "\n\n\n\nPer leggere il file usa la libreria pandas... e non dimenticarti del separatore con cui è formattato il file!",  '\n\n\n\ndf = pd.read_csv("[nome del file.tsv]", sep="\\t")', 10, 11),
        #extract doi proposto livello medium
        "4": (f" {project} - ★ EXTRACT DOI ★ ", '\n\n\nEstrai dal dataframe il DOI con cui potrai leggere la pubblicazione scientifica! Estrai la colonna ed elimina i duplicati! La colonna che contiene questa informazione si chiama "DOI"', "\n\n\n\nPrima seleziona solo la colonna che ti interessa dal dataframe... e avvolgila con una funzione per rimuovere i duplicati!", '\n\n\n\ndoi = set(df["DOI"])', 10, 11),
        "5": (f" {project} - SUITABILITY ", '\nLeggi la pubblicazione! Innanzitutto: è un progetto di metagenomica? E inoltre, in questo progetto è stato campionato il microbioma della pelle di uomo? \n\n✅ Se ad entrambe le domande hai risposto "sì", procedi a fare il prossimo step.\n\n❌ Altrimenti, se anche solo una delle due domande ha come risposta "no", segna questo progetto nel tuo report, contattaci su Classroom, e inizia pure a lavorare su un altro progetto!',\
              '\n\n🧬🧬🧬 Per capire se è un progetto è di metagenomica è utile chiedersi: "è stato campionato il microbioma? è stato sequenziato il DNA dei campioni raccolti? viene citato l approccio AMPLICON o WGS?"\n\n✌️  ✌️  ✌️  Per capire se è stato campionato il microbioma della pelle di uomo puoi guardare nei Materiali e Metodi se i soggetti dello studio sono uomini e hanno campionato siti della loro pelle!', \
                 "\n\n\n\nNon c'è una soluzione fissa in questo step, questa sfida è completamente nelle tue mani! 💫🪄", 12, 11),
        #da scrivere new columns
        "6": (f" {project} - ★ NEW COLUMNS ★ ", '\n\nEhi Data Hunter, sei arrivato allo step più critico: curare il contenuto del dataframe di metadati. Niente paura, ti spieghiamo tutto. Ti ricordiamo che le colonne da curare sono 9: \
              \n\n1) "library_strategy": la strategia di sequenziamento (AMPLICON, WGS)\n\n2) "instrument_platform": la piattaforma di sequenziamento (ILLUMINA, ION TORRENT, ...)\n\n3) "instrument_model": modello di sequenziatore (ILLUMINA MiSeq, ILLUMINA NovaSeq, ...)\
              \n\n4) "SKIOME_amplicon_target": amplicone targettato (16S, ITS, ...)\n\n5) "SKIOME_target_region": regione ipervariabile dell amplicone (V1, V3-V4, ...)\n\n6) "SKIOME_primer": primer (GTGCCAGCMGCCGCGGTAA, GGACTACNVGGGTWTCTAAT, ...)\
              \n\n7) "SKIOME_individuals_nationality": nazionalità degli individui campionati (Italy, Spain, ...)\n\n8) "SKIOME_body_site": sito del corpo campionato (hands, forehead, ...)\n\n9) "SKIOME_status": condizione o stato che si attribuisce ai soggetti campionati in base alle diverse ipotesi considerate (healthy vs disease, rural vs urban, ...) \
              \n\n\n1️⃣  Le colonne "library_strategy", "instrument_platform", "instrument_model" sono già presenti nel tuo dataframe! Controlla che l informazione che hai trovato nella pubblicazione sia uguale a quella presente nel dataframe \
              \n2️⃣  Tutte le altre colonne potrebbero esserci nel tuo dataframe ma non con certezza: devi cercarle! 🅰️  Per le colonne che esistono fai come nel punto 1: controlla che l informazione che hai trovato nella pubblicazione sia uguale a quella presente nel dataframe. 🅱️  Per le colonne che non esistono: devi crearle e compilarle con l informazione trovata!\
              \n\n\n⚠️  Se trovi che in una colonna dovrebbe essere contenuto più di un valore, per esempio hanno campionato il microbioma della pelle delle mani e del viso contattaci su Classroom e ti diremo come agire!\n⚠️  In ogni caso, se hai dubbi sul valore da compilare contattaci su Classroom!\
              \n\n\n💎 Questo è lo step più prezioso: ricercatori di tutto il mondo scaricheranno i progetti che hai curato, e daranno per scontato che le informazioni siano impeccabili. Il futuro della ricerca del microbioma della pelle di uomo è anche nelle (e sulle eheh) tue mani.', \
              '\n1️⃣  Per le colonne che già esistono, estrai la colonna dal dataframe (PS il nome della colonna è proprio come l abbiamo chiamata nel box principale!🧠 )... e poi seleziona solo i valori unici! Verifica con if se il valore estratto dalla colonna è uguale a quello che hai trovato tu nella pubblicazione! \
                \n\n2️⃣  Per le colonne da cercare, usa l informazione che hai trovato nella pubblicazione come valore da trovare nelle varie colonne del dataframe! \
                \n🅰️  Se la colonna esiste, estrai la colonna dal dataframe e poi seleziona solo i valori unici! Verifica se il valore che hai trovato nella pubblicazione è uguale a quello presente nel df: se è diverso crea una nuova colonna! \
                \n🅱️  Se la colonna non esiste, crea una nuova colonna e associa il valore che hai trovato nella pubblicazione',\
                '\n\n1️⃣\nvalore-nei-metadati = df["nome_della_colonna"].unique()\nif valore-nei-metadati == "valore-trovato-nel-paper":\n   print("EVVIVA, la colonna è compilata correttamente")\nelse:\n   print("OH NO, una nuova colonna con il valore corretto deve essere creata")\
                \n\n\n2️⃣\ncolonne = df.columns.to_list()\ncolonne_trovate=[]\n\n>>>SPIEGAZIONE: prima crea una lista delle colonne del tuo df, e poi crea una lista vuota che si riempirà delle colonne del df in cui è stato trovato il valore\
                \n\nfor colonna in colonne:\n   if "valore".lower() in colonna.lower():\n      colonne_trovate.append(colonna)\
                \n   else:\n      pass\n\n>>>SPIEGAZIONE: per ciascuna colonna presente nella lista colonne, cerca se il valore della pubblicazione è presente nella colonna. se è presente allora segna il nome della colonna in cui è stato trovato nella lista colonne_trovate. Se non è presente in quella colonna il loop continua senza segnare nulla\
                \n\n🅰️  if len(colonne_trovate)>0:\n      for colonna in colonne_trovate:\n         print(df[colonna].unique())\
                \n   else:\n      print("nessuna colonna trovata!")\n\n🅱️  df["SKIOME_nome_della_colonna"] = "valore trovato nel paper")\n\n>>>SPIEGAZIONE: se la lunghezza della lista colonne_trovate è maggiore di 0 significa che nel tuo dataframe esiste almeno una colonna contenente il valore che hai trovato nella pubblicazione. Stampa i valori contenuti in ciascuna delle colonne presenti nella lista colonne_trovate per verificare se il valore contenuto in questa/e colonna/e è lo stesso. Se non è uguale, crea una nuova colonna con il valore corretto!\
                \nInvece, se non hai trovato il valore nel dataframe, significa che nel dataframe non esiste una colonna specifica che contiene quel valore. Quindi crea una nuova colonna e riempila con il valore che hai trovato nel paper', 45, 47),
        "7": (f" {project} - SAVING FILE ", f'\n\nOra che il dataframe dei metadati è stato curato alla perfezione, è tempo di salvarlo sotto forma di file TSV!\n\nIl nome del file da salvare deve essere: "SKIOME_{project}_df.tsv"', "\n\n\nIndica il dataframe, il nome del file che vuoi salvare e il separatore delle righe!", f'\n\n\ndf.to_csv("SKIOME_{project}_df.tsv", sep="\\t", index=False)', 10, 11)
        }

        if user_input in options_dict:
            arguments = options_dict[user_input]
            curation_function(*arguments)
        elif user_input == "BACK":
            return
        elif user_input == "EXIT":
            console.print("\nGood bye, see you soon!\n", style= "bold magenta1", justify="center")
            exit()
        else:
            text = "Risposta non valida 🪇   Sei sicuro di aver digitato un numero da 1 a 7?"
            centered_text = center_text(text)
            input(centered_text)


def level_hard(project):
    while True:
        clear()
        #presentazione delle 9 opzioni di steps da fare nella manual curation
        project_file = os.path.splitext(os.path.basename(project))[0].replace(".tsv", "")
        intro_box = Panel(f"\n{project_file}", title=" SELECTED PROJECT ", style="bold", border_style="magenta1", padding=(0, 1), width=50, height=5)
        console.print(intro_box, justify="center")
        print("\n")
        options = ["[b][yellow]1. DEEPNOTE[/b]", "[b][yellow]2. IMPORT LIBRARY[/b]", "[b][yellow]3. READ DATAFRAME[/b]"]
        colors = ["yellow", "yellow", "yellow"]
        choice = [Panel(opt.center(45), border_style=color, padding=(1, 1), width=40) for opt, color in zip(options, colors)]
        console.print(Columns(choice), justify="center")
        options = ["[b][yellow]4. EXTRACT DOI[/b]", "[b][yellow]5. PROJECT SUITABILITY[/b]", "[b][yellow]★ 6. ADD NEW COLUMNS ★[/b]"]
        choice = [Panel(opt.center(45), border_style=color, padding=(1, 1), width=40) for opt, color in zip(options, colors)]
        console.print(Columns(choice), justify="center")
        options = ["[b][yellow]7. SAVE FILE[/b]"]
        choice = [Panel(opt.center(45), border_style=color, padding=(1, 1), width=40) for opt, color in zip(options, colors)]
        console.print(Columns(choice), justify="center")

        options = ["[b][cyan1]BACK[/b]", "[b][cyan1]EXIT[/b]"]
        colors = ["cyan1", "cyan1"]
        columns = options_box(options, colors)
        console.print(columns, justify="center")
        
        #scelta dello step di manual curation da fare
        text = "Quale step devi affrontare? Gli step con le stelle sono quelli dove la difficolta ora è maggiore! Digita il numero corrispondente: "
        centered_text = center_text(text)
        print("\n")
        user_input = input(centered_text).upper().strip()

        options_dict = {
        "1": (f" {project} - DEEPNOTE ", "\n\n\n\nPer iniziare, apri un nuovo Notebook cliccando sul +", "\n\n\n\n\nIn alto a sinistra vedi dove c'è scritto 'Notebooks'? Clicca sul +", "\n\n\n\nDai crediamo in te! 🫶", 10, 11),
        "2": (f" {project} - PANDAS ", "\n\n\n\nImporta la libreria pandas!", "\n\n\n\n\nPer usare una libreria in python bisogna prima importarla...", "\n\n\n\nimport pandas as pd", 10, 11),
        "3": (f" {project} - DATAFRAME ", "\n\n\n\nLeggi il file come dataframe di pandas!", "\n\n\n\nPer leggere il file usa la libreria pandas... e non dimenticarti del separatore con cui è formattato il file!",  '\n\n\n\ndf = pd.read_csv("[nome del file.tsv]", sep="\\t")', 10, 11),
        #extract doi proposto livello medium
        "4": (f" {project} - EXTRACT DOI ", '\n\n\nEstrai dal dataframe il DOI con cui potrai leggere la pubblicazione scientifica! Estrai la colonna ed elimina i duplicati! La colonna che contiene questa informazione si chiama "DOI"', "\n\n\n\nPrima seleziona solo la colonna che ti interessa dal dataframe... e avvolgila con una funzione per rimuovere i duplicati!", '\n\n\n\ndoi = set(df["DOI"])', 10, 11),
        "5": (f" {project} - SUITABILITY ", '\nLeggi la pubblicazione! Innanzitutto: è un progetto di metagenomica? E inoltre, in questo progetto è stato campionato il microbioma della pelle di uomo? \n\n✅ Se ad entrambe le domande hai risposto "sì", procedi a fare il prossimo step.\n\n❌ Altrimenti, se anche solo una delle due domande ha come risposta "no", segna questo progetto nel tuo report, contattaci su Classroom, e inizia pure a lavorare su un altro progetto!',\
              '\n\n🧬🧬🧬 Per capire se è un progetto è di metagenomica è utile chiedersi: "è stato campionato il microbioma? è stato sequenziato il DNA dei campioni raccolti? viene citato l approccio AMPLICON o WGS?"\n\n✌️  ✌️  ✌️  Per capire se è stato campionato il microbioma della pelle di uomo puoi guardare nei Materiali e Metodi se i soggetti dello studio sono uomini e hanno campionato siti della loro pelle!', \
                 "\n\n\n\nNon c'è una soluzione fissa in questo step, questa sfida è completamente nelle tue mani! 💫🪄", 12, 11),
        #da scrivere new columns
        "6": (f" {project} - ★ NEW COLUMNS ★ ", '\n\nEhi Data Hunter, sei arrivato allo step più critico: curare il contenuto del dataframe di metadati. Niente paura, ti spieghiamo tutto. Ti ricordiamo che le colonne da curare sono 9: \
              \n\n1) "library_strategy": la strategia di sequenziamento (AMPLICON, WGS)\n\n2) "instrument_platform": la piattaforma di sequenziamento (ILLUMINA, ION TORRENT, ...)\n\n3) "instrument_model": modello di sequenziatore (ILLUMINA MiSeq, ILLUMINA NovaSeq, ...)\
              \n\n4) "SKIOME_amplicon_target": amplicone targettato (16S, ITS, ...)\n\n5) "SKIOME_target_region": regione ipervariabile dell amplicone (V1, V3-V4, ...)\n\n6) "SKIOME_primer": primer (GTGCCAGCMGCCGCGGTAA, GGACTACNVGGGTWTCTAAT, ...)\
              \n\n7) "SKIOME_individuals_nationality": nazionalità degli individui campionati (Italy, Spain, ...)\n\n8) "SKIOME_body_site": sito del corpo campionato (hands, forehead, ...)\n\n9) "SKIOME_status": condizione o stato che si attribuisce ai soggetti campionati in base alle diverse ipotesi considerate (healthy vs disease, rural vs urban, ...) \
              \n\n\n1️⃣  Le colonne "library_strategy", "instrument_platform", "instrument_model" sono già presenti nel tuo dataframe! Controlla che l informazione che hai trovato nella pubblicazione sia uguale a quella presente nel dataframe \
              \n2️⃣  Tutte le altre colonne potrebbero esserci nel tuo dataframe ma non con certezza: devi cercarle! 🅰️  Per le colonne che esistono fai come nel punto 1: controlla che l informazione che hai trovato nella pubblicazione sia uguale a quella presente nel dataframe. 🅱️  Per le colonne che non esistono: devi crearle e compilarle con l informazione trovata!\
              \n\n\n⚠️  Se trovi che in una colonna dovrebbe essere contenuto più di un valore, per esempio hanno campionato il microbioma della pelle delle mani e del viso contattaci su Classroom e ti diremo come agire!\n⚠️  In ogni caso, se hai dubbi sul valore da compilare contattaci su Classroom!\
              \n\n\n💎 Questo è lo step più prezioso: ricercatori di tutto il mondo scaricheranno i progetti che hai curato, e daranno per scontato che le informazioni siano impeccabili. Il futuro della ricerca del microbioma della pelle di uomo è anche nelle (e sulle eheh) tue mani.', \
              '\n1️⃣  Per le colonne che già esistono, puoi creare un dizionario dove la key è il nome della colonna e il value è il valore che hai trovato nel paper. A questo punto puoi fare un ciclo for tra gli elementi del dizionario in modo da verificare se il valore trovato nel paper per una determinata colonna è uguale al valore che si trova nella colonna del dataframe \
                \n\n2️⃣  Per le colonne da cercare, usa l informazione che hai trovato nella pubblicazione come valore da trovare nelle varie colonne del dataframe! \
                \n🅰️  Se la colonna esiste, estrai la colonna dal dataframe e poi seleziona solo i valori unici! Verifica se il valore che hai trovato nella pubblicazione è uguale a quello presente nel df: se è diverso crea una nuova colonna! \
                \n🅱️  Se la colonna non esiste, crea una nuova colonna e associa il valore che hai trovato nella pubblicazione',\
                '\n\n1️⃣\ndizionario = {"library_strategy" : "valore-trovato-nel-paper",  "instrument_platform" : "valore-trovato-nel-paper", "instrument_model" : "valore-trovato-nel-paper"}\nfor x,y in dizionario.items():\n   valore-nei-metadati = df[x].unique()\n   if valore-nei-metadati == y\n      print("EVVIVA, la colonna è compilata correttamente")\n   else:\n      print(valore-nei-metadati)\nprint(OH NO, una nuova colonna con il valore corretto deve essere creata)\
                \n\n\n2️⃣\ncolonne = df.columns.to_list()\ncolonne_trovate=[]\n\n>>>SPIEGAZIONE: prima crea una lista delle colonne del tuo df, e poi crea una lista vuota che si riempirà delle colonne del df in cui è stato trovato il valore\
                \n\nfor colonna in colonne:\n   if "valore".lower() in colonna.lower():\n      colonne_trovate.append(colonna)\
                \n   else:\n      pass\n\n>>>SPIEGAZIONE: per ciascuna colonna presente nella lista colonne, cerca se il valore della pubblicazione è presente nella colonna. se è presente allora segna il nome della colonna in cui è stato trovato nella lista colonne_trovate. Se non è presente in quella colonna il loop continua senza segnare nulla\
                \n\n🅰️  if len(colonne_trovate)>0:\n      for colonna in colonne_trovate:\n         print(df[colonna].unique())\
                \n   else:\n      print("nessuna colonna trovata!")\n\n🅱️  df["SKIOME_nome_della_colonna"] = "valore trovato nel paper")\n\n>>>SPIEGAZIONE: se la lunghezza della lista colonne_trovate è maggiore di 0 significa che nel tuo dataframe esiste almeno una colonna contenente il valore che hai trovato nella pubblicazione. Stampa i valori contenuti in ciascuna delle colonne presenti nella lista colonne_trovate per verificare se il valore contenuto in questa/e colonna/e è lo stesso. Se non è uguale, crea una nuova colonna con il valore corretto!\
                \nInvece, se non hai trovato il valore nel dataframe, significa che nel dataframe non esiste una colonna specifica che contiene quel valore. Quindi crea una nuova colonna e riempila con il valore che hai trovato nel paper', 45, 52),
        "7": (f" {project} - SAVING FILE ", f'\n\nOra che il dataframe dei metadati è stato curato alla perfezione, è tempo di salvarlo sotto forma di file TSV!\n\nIl nome del file da salvare deve essere: "SKIOME_{project}_df.tsv"', "\n\n\nIndica il dataframe, il nome del file che vuoi salvare e il separatore delle righe!", f'\n\n\ndf.to_csv("SKIOME_{project}_df.tsv", sep="\\t", index=False)', 10, 11)
        }

        if user_input in options_dict:
            arguments = options_dict[user_input]
            curation_function(*arguments)
        elif user_input == "BACK":
            return
        elif user_input == "EXIT":
            console.print("\nGood bye, see you soon!\n", style= "bold magenta1", justify="center")
            exit()
        else:
            text = "Risposta non valida 🪇   Sei sicuro di aver digitato un numero da 1 a 7?"
            centered_text = center_text(text)
            input(centered_text)