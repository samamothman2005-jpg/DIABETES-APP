<!DOCTYPE html>
<html>
<head>
    <title>Diabetes Prediction</title>

    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial;
            
            background: 
            linear-gradient(rgba(255,255,255,0.7), rgba(255,255,255,0.7)),
            url("https://images.unsplash.com/photo-1579154204601-01588f351e67");

            background-size: cover;
            background-position: center;
        }

        .container {
            width: 350px;
            margin: 80px auto;
            padding: 30px;
            background: white;
            border-radius: 15px;
            box-shadow: 0 0 20px rgba(0,0,0,0.2);
            text-align: center;
        }

        h2 {
            margin-bottom: 20px;
        }

        input {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            border-radius: 8px;
            border: 1px solid #ccc;
        }

        button {
            width: 100%;
            padding: 10px;
            margin-top: 10px;
            background: #4CAF50;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }

        button:hover {
            background: #45a049;
        }

        .result {
            margin-top: 15px;
            font-weight: bold;
        }

        .importance {
            margin-top: 10px;
            text-align: left;
        }
    </style>
</head>

<body>

<div class="container">
    <h2>🩸 Diabetes Prediction</h2>

    <form action="/predict" method="post">
        <input type="text" name="glucose" placeholder="Glucose">
        <input type="text" name="bmi" placeholder="BMI">
        <input type="text" name="age" placeholder="Age">
        <input type="text" name="bp" placeholder="Blood Pressure">
        <input type="text" name="insulin" placeholder="Insulin">

        <button type="submit">Predict</button>
    </form>

    <div class="result">
        Result: {{ prediction }} %
    </div>

    <div class="importance">
        <h4>Feature Importance:</h4>
        {% for f, i in importance %}
            <div>{{ f }} : {{ i|round(2) }} %</div>
        {% endfor %}
    </div>

</div>

</body>
</html>