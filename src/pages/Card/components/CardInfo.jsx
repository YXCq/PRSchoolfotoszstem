import "../card.css"
export function CardInfo () {
    return (
        <div className="CardInfo">
            <input type="text" value="Full Name" readOnly />
            <input type="text" value="E-mail:" readOnly />
        </div>
    )
}

// export function Photo() {
//     return (
//         <div className="Photo">
//             <img src={photo} alt=""/>
//         </div>
//     )
// }