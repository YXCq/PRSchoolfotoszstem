import React from "react";

function login_card() {
    return (
        <div className="login_card">
            <div className="form">
                <h1>Log In</h1>
                <div className="form_card">
                    <form>
                        <input type="text" id="name" name="name" placeholder="Name"/>

                        <input type="password" id="password" name="password" placeholder="Password"/>

                        <button type="submit">Log In to your account</button>
                    </form>
                </div>
            </div>
        </div>
    );
}

export default login_card;