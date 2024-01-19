
import Card from "./pages/Card/Card";
import Main from "./pages/Main/Main";
import Login from "./pages/Login/Login";
import Register from "./pages/Register/Register";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/Login" element={<Login />} />
                <Route path="/card" element={<Card />} />
                <Route path="/" element={<Main />} />
                <Route path="/register" element={<Register/>}/>
            </Routes>
        </Router>
    );
}

export default App;
