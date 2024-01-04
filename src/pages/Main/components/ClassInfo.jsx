import "../main.css"
export const ClassInfo = () => {
    return (
        <div className="classInfo">
            <h1>Class <br/> Information</h1>
            <div className="info">
                <input type="text" value="Class number: 3E2" readOnly />
                <input type="text" value="Class Teacher: Markus Vonanten" readOnly />
                <input type="text" value="Class year: 2021-2024" readOnly />
            </div>
        </div>
    )
}