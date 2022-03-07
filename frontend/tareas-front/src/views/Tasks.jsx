import React, { useEffect, useState } from 'react'
import decode from 'jwt-decode'
import { listarTarea } from '../services/tarea.service'
import { Task } from '../components/Task'

export const Tasks = () => {
  // TODO: useContext para traer la información del usuario
  const token = localStorage.getItem('token')
  const [user, setUser] = useState()
  const [tareas, setTareas] = useState([])

  useEffect(() => {
    setUser(decode(token))
    async function traerTareas() {
      try {
        const { data } = await listarTarea(token)
        console.log(data);
        setTareas(data)
      } catch (e) {
        alert("Error al traer la información")
      }
    }
    traerTareas()
  }, [token])

  return (
    <div>
      <div>
        <h1>
          Hola {user?.nombre} {user?.apellido}
        </h1>
      </div>
      <div>
        {tareas.map((tarea) => (<Task key={tarea._id} {...tarea} />))}
      </div>
    </div>
  )
}
