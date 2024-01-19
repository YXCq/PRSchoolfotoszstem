import React, { useState } from "react";
import axios from "axios";

const LoginCard = () => {
    const [login, setLogin] = useState("");
    const [password, setPassword] = useState("");
    const [response, setResponse] = useState(null);
    const [error, setError] = useState(null);

    const handleLogin = async () => {
        try {
            const response = await axios.post("http://127.0.0.1:8000/user/login", {
                login: login,
                password: password,
            });

            // Assuming the response contains relevant data
            setResponse(response.data);
        } catch (error) {
            console.error("Error logging in:", error);
            setError("An error occurred during login. Please try again.");
        }
    };

    return (
        <div>
            <h1>React App</h1>
            <div>
                <label>Login:</label>
                <input type="text" value={login} onChange={(e) => setLogin(e.target.value)} />
            </div>
            <div>
                <label>Password:</label>
                <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
            </div>
            <button onClick={handleLogin}>Login</button>

            {error && <p style={{ color: "red" }}>{error}</p>}

            {response && (
                <div>
                    <h2>Response from Server:</h2>
                    <p>Login: {response.data}</p>
                    <p>Password: {response.password}</p>
                </div>
            )}
        </div>
    );
};

export default LoginCard;
