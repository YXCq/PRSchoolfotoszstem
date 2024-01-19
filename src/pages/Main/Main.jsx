import {Header} from "./components/Header";
import {ClassInfo} from "./components/ClassInfo";
import {OwnInfo} from "./components/OwnInfo";
import {Edit} from "./components/Edit";
import {CardInfo} from "./components/CardInfo";
import {ParentCard} from "./components/ParentCard";
import {Footer} from "./components/Footer";

const Main = () => {
    return (
        <div className="main">
        <Header />
        <ClassInfo />
        <OwnInfo />
        <Edit />
        <ParentCard />
        <Footer />
        </div>
    )
}

export default Main;