import React, {useState, useEffect} from 'react';
import {Navigate} from 'react-router-dom';
import {jwtDecode} from 'jwt-decode';
import api from '../api';
import { ACCESS_TOKEN, REFRESH_TOKEN } from '../constants';

function ProtectedRoute({children}) {
    const [isAutorized, setIsAutorized] = useState(null);

    useEffect(() => {
        authtoken().catch((error) => {
                console.log(error);
                setIsAutorized(false);
            }
        )
    } , []);

    const refreshToken = async () =>{
        const refreshToken = localStorage.getItem(REFRESH_TOKEN);
        try{
            const res = await api.post('/authen/refresh/', 
                {refreshToken}
            );
            if (res.status === 200) {
                localStorage.setItem(ACCESS_TOKEN, res.data.accessToken);
                setIsAutorized(true);
            } else {
                setIsAutorized(false);
            }
        }
        
        catch(error){
            console.log(error);
            setIsAutorized(false);
        }
    }

    const authtoken = async () => {
        const token = localStorage.getItem(ACCESS_TOKEN);
        
        if (!token) {
            setIsAutorized(false);
            return;
        }

        const decode = jwtDecode(token);
        const tokenExpiration = decode.exp;
        const currentTime = Date.now() / 1000;

        if(tokenExpiration < currentTime) {
            console.log("this one")
            await refreshToken();
        }else{
            setIsAutorized(true);
        }
    }

    if (isAutorized == null) {
        return <div> ...loading </div>
    }


    return isAutorized ? children : <Navigate to="/login" />;
}

export default ProtectedRoute;