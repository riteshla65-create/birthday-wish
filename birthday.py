from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Happy Birthday Deepak!</title>
    <style>
        body {
            background: linear-gradient(rgba(26, 26, 46, 0.7), rgba(22, 33, 62, 0.8)), 
                        url('https://images.unsplash.com/photo-1530103862676-de8c9debad1d?q=80&w=1000&auto=format&fit=crop');
            background-size: cover;
            background-position: center;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            overflow: hidden;
            position: relative;
        }
        .card {
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 50px 40px;
            border-radius: 25px;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
            text-align: center;
            max-width: 450px;
            color: white;
            z-index: 10;
            animation: superPop 1.2s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
        }
        h1 {
            color: #ff477e;
            font-size: 3.5rem;
            margin-bottom: 5px;
            text-shadow: 0 0 15px rgba(255, 71, 126, 0.8);
        }
        .special-msg {
            font-style: italic;
            color: #00ffff;
            font-size: 1.4rem;
            margin-bottom: 25px;
            text-shadow: 0 0 8px rgba(0, 255, 255, 0.6);
        }
        .btn {
            background: linear-gradient(45deg, #ff477e, #ff85a1);
            color: white;
            border: none;
            padding: 15px 35px;
            font-size: 1.2rem;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: bold;
            box-shadow: 0 5px 20px rgba(255, 71, 126, 0.5);
        }
        .btn:hover {
            transform: scale(1.1) translateY(-3px);
            box-shadow: 0 10px 30px rgba(255, 71, 126, 0.8);
        }
        .modal-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.85);
            backdrop-filter: blur(8px);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 100;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.5s ease;
        }
        .modal-box {
            background: linear-gradient(135deg, #2b1055, #7597de);
            border: 2px solid #ff477e;
            padding: 40px;
            border-radius: 20px;
            text-align: center;
            max-width: 450px;
            color: white;
            box-shadow: 0 0 40px rgba(255, 71, 126, 0.6);
            transform: scale(0.5) rotate(-10deg);
            transition: transform 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }
        .modal-overlay.active {
            opacity: 1;
            pointer-events: auto;
        }
        .modal-overlay.active .modal-box {
            transform: scale(1) rotate(0deg);
        }
        .modal-box h2 {
            color: #fffb00;
            font-size: 2.3rem;
            text-shadow: 0 0 10px rgba(255, 251, 0, 0.5);
        }
        .close-btn {
            background: #ff477e;
            color: white;
            border: none;
            padding: 10px 25px;
            font-size: 1rem;
            border-radius: 20px;
            cursor: pointer;
            margin-top: 20px;
            font-weight: bold;
        }
        .balloon {
            position: absolute;
            width: 35px;
            height: 45px;
            border-radius: 50% 50% 50% 50% / 40% 40% 60% 60%;
            bottom: -60px;
            opacity: 0.8;
            animation: floatUp 7s linear infinite;
        }
        .balloon::after {
            content: "▲";
            color: inherit;
            font-size: 10px;
            position: absolute;
            bottom: -6px;
            left: 13px;
        }
        @keyframes floatUp {
            0% { transform: translateY(0) rotate(0deg); }
            100% { transform: translateY(-120vh) rotate(35deg); }
        }
        @keyframes superPop {
            0% { transform: scale(0.3); opacity: 0; }
            100% { transform: scale(1); opacity: 1; }
        }
    </style>
</head>
<body>
    <div id="balloon-container"></div>
    <div class="card">
        <h1>🎂 Deepak 🎂</h1>
        <div class="special-msg">It is only for you</div>
        <p>Aapke liye ek digital surprise taiyar hai!</p>
        <button class="btn" onclick="openPopup()">Tap to Open 🎁</button>
    </div>
    <div class="modal-overlay" id="customPopup">
        <div class="modal-box">
            <h2>🎉 HAPPY BIRTHDAY DEEPAK! 🥳</h2>
            <p>🎂🎈✨</p>
            <p>Bhai tu jiyo hazaron saal! Din ekdum kadak aur shandaar hona chahiye tera!</p>
            <p>Enjoy your special day to the fullest, lots of love! 🥂</p>
            <button class="close-btn" onclick="closePopup()">Thank You! ❤️</button>
        </div>
    </div>
    <script>
        function openPopup() { document.getElementById('customPopup').classList.add('active'); }
        function closePopup() { document.getElementById('customPopup').classList.remove('active'); }
        function createBalloons() {
            const container = document.getElementById('balloon-container');
            const colors = ['#ff477e', '#ff7096', '#00ffff', '#fffb00', '#ff0055', '#3498db', '#2ecc71', '#9b59b6'];
            for (let i = 0; i < 45; i++) {
                const balloon = document.createElement('div');
                balloon.className = 'balloon';
                balloon.style.left = Math.random() * 100 + 'vw';
                const randomColor = colors[Math.floor(Math.random() * colors.length)];
                balloon.style.backgroundColor = randomColor;
                balloon.style.color = randomColor;
                balloon.style.animationDelay = Math.random() * 6 + 's';
                balloon.style.animationDuration = (Math.random() * 4 + 5) + 's';
                container.appendChild(balloon);
            }
        }
        window.onload = createBalloons;
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)