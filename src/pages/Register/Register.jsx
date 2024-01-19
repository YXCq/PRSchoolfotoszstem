import React, { useState } from "react";
import {
    Button,
    Center,
    ChakraProvider,
    FormControl,
    FormLabel,
    Input,
    VStack,
} from "@chakra-ui/react";
import axios from "axios";  // Import Axios

const Register = () => {
    const [login, setLogin] = useState("");
    const [email, setEmail] = useState("");
    const [classroom, setClassroom] = useState("");
    const [password, setPassword] = useState("");
    const [registrationError, setRegistrationError] = useState(null);

    const handleRegister = async () => {
        try {
            const response = await axios.post("http://127.0.0.1:8000/user/register", {
                login: login,
                email: email,
                classroom: classroom,
                password: password,
            });

            if (response.status === 200) {
                const data = response.data;
                console.log("Full Response:", data);

                // Check for specific success criteria from the server response
                if (data.success) {
                    // Perform actions for a successful registration, e.g., redirect
                } else {
                    setRegistrationError("Registration failed");
                }
            } else {
                console.error("Registration failed");
                setRegistrationError("Registration failed. Please try again.");
            }
        } catch (error) {
            console.error("Error during registration:", error);
            setRegistrationError("An unexpected error occurred. Please try again later.");
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
                    <FormControl id="email">
                        <FormLabel>Email</FormLabel>
                        <Input
                            type="email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                        />
                    </FormControl>
                    <FormControl id="classroom">
                        <FormLabel>Classroom</FormLabel>
                        <Input
                            type="text"
                            value={classroom}
                            onChange={(e) => setClassroom(e.target.value)}
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
                    <Button size="lg" onClick={handleRegister}>
                        Register
                    </Button>
                    {registrationError && <p style={{ color: "red" }}>{registrationError}</p>}
                </VStack>
            </Center>
        </ChakraProvider>
    );
};

export default Register;
