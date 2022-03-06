import React from 'react'
import { useNavigate, Link } from 'react-router-dom'

export const Index = () => {
    const navigate = useNavigate()

    const login = (e) => {
        navigate('/login')
    }

    return (
        <div>
            <p>
                Bienvenido al front de las tareas 😬
            </p>
            <p>
                ¿Tienes cuenta?
                <button onClick={login}>Inicia Sesión</button>
                <Link to='/register'>Crea una nueva cuenta</Link>
            </p>
        </div>

    )
}
