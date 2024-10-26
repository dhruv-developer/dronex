import React from 'react';
import { Map, GoogleApiWrapper, Marker } from 'google-maps-react';

const MapView = ({ google }) => {
    return (
        <Map
            google={google}
            zoom={10}
            initialCenter={{ lat: -1.2921, lng: 36.8219 }}
        >
            <Marker position={{ lat: -1.2921, lng: 36.8219 }} />
        </Map>
    );
};

export default GoogleApiWrapper({
    apiKey: 'AIzaSyAxEYPIcz4RCV2q6VC3JbMmTQahq9yVaG4',
})(MapView);
