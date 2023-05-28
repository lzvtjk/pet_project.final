import play

play.set_backdrop("white")

@play.when_program_starts #функція для початку програми 
def start():
    global player , speech
    text1 = play.new_text(words = " g - glasses , p - play guitar, c - cry" , x = 0 , y = 260 , font_size = 40)
    text2 = play.new_text(words = " j - jump , m - meet friend , h - hello" , x = 0 , y = 230 , font_size = 40)
    player = play.new_image(image = "kuromi.jpg" , x = 0 , y = 0 , size = 70 )
    speech = play.new_text(words = "Hello who are you" , x = 0 , y = -250)

@play.repeat_forever #повторювати завжди(ігровий цикл)
async def do():
    if play.key_is_pressed("g") or play.key_is_pressed("G"):
        speech.words = "are you serious"
        await play.timer(3.0)
        player.size = 60
        player.image = "Glasses kuromi.jpg"
        speech.words = "cool bro"
    if play.key_is_pressed("p") or  play.key_is_pressed("P"):
        player.size = 70
        player.image = "insidious kuromi.jpg"
        speech.words = "maybe something else"
        await play.timer(3.0)
        speech.words = "well,if you really want,ok"
        player.size = 60
        player.image = "Guitar kuromi.jpg"
        speech.words = "ПЕС ПАТРОН ПЕС ПАТРОН"
    if play.key_is_pressed("c") or  play.key_is_pressed("C"):
        player.size = 70
        player.image = "Heart kuromi.jpg"
        speech.words = "i'm so sad"
        await play.timer(3.0)
        player.image = "Whining kuromi.jpg"
    if play.key_is_pressed("j") or  play.key_is_pressed("J"):
        player.size = 70
        player.image = "insidious kuromi.jpg"
        speech.words = "i'm tired"
        await play.timer(3.0)
        speech.words = "i'm kidding?"
        player.image = "Joyful kuromi.jpg"
        await play.timer(3.0)
        speech.words = "enough, you can jump on your own"
        player.image = "Lol kuromi.jpg"
    if play.key_is_pressed("m") or  play.key_is_pressed("M"):
        player.size = 70
        player.image = "with kuromi.jfif"
        speech.words = "she's so shy"
        await play.timer(3.0) 
        player.image = "w kuromi.jfif" 
    if play.key_is_pressed("h") or  play.key_is_pressed("H"):
        player.size = 120
        player.image = "k kuromi.jfif"
        speech.words = "who are you?"
        await play.timer(3.0)
        speech.words = "ohh that's you"
        player.image = "hello kuromi.jfif"


play.start_program() #запуск програми


#jump=True
#jump = True
#if play.key_is_pressed("j") and jump == True:
#if play.key_is_pressed("j") and jump == :