# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("Johan Fidelis")
define sc1 = Character("Aina Alkan")
define sc2 = Character("Alexandra Galkin")
define ana = Character("Annem", color="#ffcccc")
# The game starts here.

label start:
    play music "audio/ost1.mp3" loop
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    mc "Babamı daha yenigömdüm. Dün mü, evelsi gün mü, hatırlayamıyorum."

    mc "Dışarı çıkıp hayatıma devam etmek istiyorum ama yapabilir miyim, bilmiyorum."

    mc "Hayat acımasız, bu yüzden eğer tanrı varsa bu tanrıya inanmayı reddediyorum."
    # This ends the game.

    show mc normal
    menu:

        "Direkt okula git":
            jump okulgit
        "Önce mutfağa git":
            jump mtfgit
    
    

    label okulgit:

    $ menu_flag = True

    mc "Öfff, sabahın köründe okula mı gidilir?"
    

    jump oyundevam

    label mtfgit:

    $ menu_flag = False

    ana "Oğlum gel kahvaltı hazır."
    
    mc "Tamamdır, geliyorum şimdi."
    mc "Bekle azıcık."
    "*Merdivenden inme sesleri*"

    ana "Çok uzun sürdü, geç kalacaklsın! Haydi hızlıca kahvaltını yap."
    
    mc "Anne daha yarım saat falan var, rahat ol."

    ana "Ya sen yemeğini bitirene kadar çoktan yarım saat geçmiş olacak, hadi! "

    "Ah, benim zavallı ama güçlü annem."
    "Nasıl kocanın cenazesinden birkaç gün sonra bu kadar enerjik olabiliyorsun?"
    "Bazenleri sana gerçekten hayran kalıyorum"

    ana "Oğlum boş gözlerle bakmayı kes, hızlıca bitir şu yemeğini!"

    "Menemen, babamın en sevdiği yemek idi sanırım."
    "Mark Fidelis, Şahsen seninle yakın değildim ama senden nefret de etmedim."
    mc "Eline sağlık annem, enfes olmuş."

    ana "Afiyet olsun sana da civcivim."

    "Normalde 'civcimim' demesini sevmem lakin bu gün laf etmeyeceğim sanırım."

    "*Ayakkabı giyme sesleri*"

    mc "Anne, ben çıktım."

    ana "Bay bay oğlum, kendine dikkat et!"

    jump oyundevam

    label oyundevam:
    "*Bisiklet sesleri*"
    "*Bisiklet sesleri*"
    "*Bisiklet sesleri...*"
    mc "Bugün de şu lanet okula da geldim, ha."
    return
