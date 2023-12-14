import photo from "../../img/Photo.png"

export const OwnInfo = () => {
    return (
        <div className="ownInfo">
            <img src={photo} alt=""/>
            <img src={photo} alt=""/>
            <input type="text" value="Full Name" readOnly />
            <input type="text" value="E-mail:" readOnly />
        </div>
    )
}