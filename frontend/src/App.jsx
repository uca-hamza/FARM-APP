import React from 'react'
import { BrowserRouter , Routes, Route, Navigate } from 'react-router-dom';
import ProtectedRoute from './components/ProtectedRoute';
import Login from './pages/auth/Login';
import Register from './pages/auth/Register';
import Home from './pages/Home';
import NotFound from './pages/NotFound';

function Logout() {
  localStorage.clear();
  return <Navigate to="/login" />;
}

function ResisterAndLogout(){
  localStorage.clear();
  return <Register route="authen/register/" />;
}

function App() {

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route 
            path="/"
            element={
              <ProtectedRoute>
                <Home />
              </ProtectedRoute>
              }
          />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<ResisterAndLogout />} />
          <Route path="/logout" element={<Logout />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
