import React from 'react';
import { CardInfo } from "./CardInfo";

export const ParentCard = () => {
    return (
        <div className="parentCardContainer">
            <div className="block-one">
                <CardInfo />
                <CardInfo />
                <CardInfo />
                <CardInfo />
                <CardInfo />
                <CardInfo />
            </div>
            <div className="block-one">
                <CardInfo />
                <CardInfo />
                <CardInfo />
                <CardInfo />
                <CardInfo />
                <CardInfo />
            </div>
            <div className="block-one">
                <CardInfo />
                <CardInfo />
                <CardInfo />
                <CardInfo />
                <CardInfo />
                <CardInfo />
            </div>
            <div className="block-final">
                <CardInfo />
                <CardInfo />
            </div>
        </div>

    );
};