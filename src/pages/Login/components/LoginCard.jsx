import React, { useState } from "react";
import axios from "axios";
import {
    Button,
    Center,
    ChakraProvider,
    FormControl,
    FormLabel,
    Input,
    VStack,
} from "@chakra-ui/react";

const Login = () => {
    const [login, setLogin] = useState("");
    const [password, setPassword] = useState("");
    const [loginError, setLoginError] = useState(null);

    const handleLogin = async () => {
        try {
            const response = await axios.post("http://127.0.0.1:8000/user/login", {
                login: login,
                password: password,
            });

            if (response.status === 200) {
                const data = response.data;
                console.log("Full Response:", data);

                // Check for specific success criteria from the server response
                if (data.success) {
                    // Perform actions for a successful login, e.g., redirect
                } else {
                    setLoginError("Invalid credentials");
                }
            } else {
                console.error("Login failed");
                setLoginError("Login failed. Please try again.");
            }
        } catch (error) {
            console.error("Error during login:", error);
            setLoginError("An unexpected error occurred. Please try again later.");
        }
    };


    return (
        <ChakraProvider>
            <Center>
                <VStack>
                    <FormControl id="login">
                        <FormLabel>Login</FormLabel>
                        <Input
                            type="text"
                            value={login}
                            onChange={(e) => setLogin(e.target.value)}
                        />
                    </FormControl>
                    <FormControl id="password">
                        <FormLabel>Password</FormLabel>
                        <Input
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                    </FormControl>
                    <Button size="lg" onClick={handleLogin}>
                        Login
                    </Button>
                    {loginError && <p style={{ color: "red" }}>{loginError}</p>}
                </VStack>
            </Center>
        </ChakraProvider>
    );
};

export default Login;










// import React, { useState } from "react";
// import { useNavigate } from "react-router-dom";
// import axios from "axios";
//
// function LoginCard() {
//     const [login, setLogin] = useState("");
//     const [password, setPassword] = useState("");
//     const [isLoggedIn, setIsLoggedIn] = useState(false);
//     const [error, setError] = useState("");
//     const history = useNavigate();
//
//     const handleSubmit = async (e) => {
//         e.preventDefault();
//         try {
//             const response = await axios.post("http://127.0.0.1:8000/user/login", {
//                 login,
//                 password,
//             });
//
//             if (response.status === 200) {
//                 const data = response.data;
//
//                 // Assuming your backend sends an access_token upon successful login
//                 if (data.access_token) {
//                     setIsLoggedIn(true);
//                     history.push("/Main"); // Redirect to /Main
//                     // Optionally, you can store the token in a more secure way (e.g., cookies or local storage)
//                 } else {
//                     setIsLoggedIn(false);
//                     setError("Invalid credentials");
//                 }
//             } else {
//                 setIsLoggedIn(false);
//                 setError("Invalid credentials");
//             }
//         } catch (error) {
//             console.error("Login error:", error);
//             setError("An error occurred");
//         }
//     };
//
//     return (
//         <div className="login_card">
//             <div className="form">
//                 <h1>Log In</h1>
//                 <div className="form_card">
//                     {isLoggedIn ? (
//                         <p>You are logged in!</p>
//                     ) : (
//                         <form onSubmit={handleSubmit}>
//                             <input
//                                 type="text"
//                                 id="login"
//                                 name="login"
//                                 placeholder="Login"
//                                 value={login}
//                                 onChange={(e) => setLogin(e.target.value)}
//                             />
//                             <input
//                                 type="password"
//                                 id="password"
//                                 name="password"
//                                 placeholder="Password"
//                                 value={password}
//                                 onChange={(e) => setPassword(e.target.value)}
//                             />
//                             <button type="submit">Log In to your account</button>
//                             {error && <p className="error">{error}</p>}
//                         </form>
//                     )}
//                 </div>
//             </div>
//         </div>
//     );
// }
//
// export default LoginCard;
