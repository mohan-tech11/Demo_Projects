<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Auth Portal | Login & Sign In</title>
    <style>
        
        :root {
            --primary-color: #4facfe;
            --secondary-color: #00f2fe;
            --text-color: #333;
            --bg-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: var(--bg-gradient);
            overflow: hidden;
        }

        .container {
            background: rgba(255, 255, 255, 0.9);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
            width: 100%;
            max-width: 400px;
            backdrop-filter: blur(10px);
        }

        h2 {
            text-align: center;
            margin-bottom: 1.5rem;
            color: var(--text-color);
        }

        .form-group {
            margin-bottom: 1.2rem;
        }

        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 600;
            font-size: 0.9rem;
        }

        input, select {
            width: 100%;
            padding: 0.8rem;
            border: 1px solid #ddd;
            border-radius: 8px;
            outline: none;
            transition: border-color 0.3s;
        }

        input:focus, select:focus {
            border-color: var(--primary-color);
        }

        button {
            width: 100%;
            padding: 0.9rem;
            border: none;
            border-radius: 8px;
            background: var(--primary-color);
            color: white;
            font-size: 1rem;
            font-weight: bold;
            cursor: pointer;
            transition: opacity 0.3s;
        }

        button:hover {
            opacity: 0.9;
        }

        .toggle-link {
            text-align: center;
            margin-top: 1rem;
            font-size: 0.85rem;
        }

        .toggle-link a {
            color: var(--primary-color);
            text-decoration: none;
            font-weight: bold;
        }

        /* Hide the Sign In form by default */
        #signin-form {
            display: none;
        }
    </style>
</head>
<body>

    <div class="container">
        <div id="login-form">
            <h2>Welcome Back</h2>
            <form>
                <div class="form-group">
                    <label>Username</label>
                    <input type="text" placeholder="Enter username" required>
                </div>
                <div class="form-group">
                    <label>Password</label>
                    <input type="password" placeholder="••••••••" required>
                </div>
                <button type="submit">Login</button>
            </form>
            <div class="toggle-link">
                Don't have an account? <a href="#" onclick="toggleForm()">Sign Up</a>
            </div>
        </div>

        <div id="signin-form">
            <h2>Create Account</h2>
            <form>
                <div class="form-group">
                    <label>Full Name</label>
                    <input type="text" placeholder="John Doe" required>
                </div>
                <div class="form-group">
                    <label>Phone Number</label>
                    <input type="tel" placeholder="+1 234 567 890" required>
                </div>
                <div class="form-group">
                    <label>User Profession</label>
                    <select required>
                        <option value="" disabled selected>Select your status</option>
                        <option value="civilian">Civilian</option>
                        <option value="official">Official (MLA / MP)</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>New Password</label>
                    <input type="password" placeholder="Create password" required>
                </div>
                <button type="submit">Register</button>
            </form>
            <div class="toggle-link">
                Already registered? <a href="#" onclick="toggleForm()">Login</a>
            </div>
        </div>
    </div>

    <script>
        function toggleForm() {
            const login = document.getElementById('login-form');
            const signin = document.getElementById('signin-form');
            
            if (login.style.display === "none") {
                login.style.display = "block";
                signin.style.display = "none";
            } else {
                login.style.display = "none";
                signin.style.display = "block";
            }
        }
    </script>
</body>
</html>