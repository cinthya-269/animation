import turtle
import random
import time

# Membuat layar
layar = turtle.Screen()
layar.setup(800, 600)
layar.bgcolor("#10152F")
layar.title("Animasi Langit Malam")
layar.tracer(0)

# Membuat objek gambar
gambar = turtle.Turtle()
gambar.hideturtle()
gambar.speed(0)
gambar.penup()

# Membuat bintang secara acak
bintang = []

for i in range(50):
    x = random.randint(-380, 380)
    y = random.randint(-270, 270)
    ukuran = random.randint(2, 6)
    bintang.append((x, y, ukuran))

# Menggambar bulan
gambar.goto(220, 150)
gambar.color("#FFE89A")
gambar.dot(100)

# Membuat efek bulan sabit
gambar.goto(245, 175)
gambar.color("#10152F")
gambar.dot(85)

# Animasi bintang
warna = ["white", "#FFF2A6", "#A8D8FF"]

try:
    while True:
        gambar.clear()

        # Menggambar bulan lagi
        gambar.goto(220, 150)
        gambar.color("#FFE89A")
        gambar.dot(100)

        gambar.goto(245, 175)
        gambar.color("#10152F")
        gambar.dot(85)

        # Menggambar bintang
        for x, y, ukuran in bintang:
            gambar.goto(x, y)
            gambar.color(random.choice(warna))
            gambar.dot(ukuran)

        layar.update()
        time.sleep(0.4)

except turtle.Terminator:
    pass