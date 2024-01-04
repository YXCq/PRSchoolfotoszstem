import Photo from './Photo.png'

export const CardInfo = () => {
    return (
        <div className="cardInfo">
            <img src={Photo} alt=""/>
            <img src={Photo} alt=""/>
            <input type="text" value="Full Name:" readOnly />
            <input type="text" value="Phone Number:" readOnly />
            <input type="text" value="E-mail:" readOnly />
        </div>
    )
}