import React, {useEffect, useState} from "react";
import "./login.css"
import Goals from "./components/goals";
import LoginCard from "./components/LoginCard";
import Find_classmates from "./components/find_classmates";
import axios from "axios";

function Login() {
    return (
        <div className="login">
            <Goals />
            <LoginCard />
            <Find_classmates />
        </div>
    );
}

export default Login;