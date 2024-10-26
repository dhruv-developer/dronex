import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Dashboard = () => {
    const [drones, setDrones] = useState([]);

    useEffect(() => {
        axios.get("http://localhost:8000/drones")
            .then(response => setDrones(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <div className="p-4">
            <h1 className="text-2xl font-bold">Drone Dashboard</h1>
            <ul>
                {drones.map(drone => (
                    <li key={drone.id}>{drone.name} - {drone.status}</li>
                ))}
            </ul>
        </div>
    );
};

export default Dashboard;
