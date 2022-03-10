//formas de import
import express, { json } from "express"; //solo sirve si se coloca en package.json: "type":"module"  (luego de main)
// const express = require("express");
const app = express();
// middleware > es un intermediario entre todas las peticiones que se realicen a determinado endpoint o si no se indica a todas las peticiones de mi API
// que mi application de express podra entender toda la informacion enviada por el cliente siempre y cuando sea un json
app.use(json());
const puerto = 3000;
const productos = [
  {
    nombre: "leche de almendras",
    precio: 9.5,
    estado: true,
  },
];

// cuando se use el método get con la ruta / el funcionamiento es el del callback ()=>{}
app.get("/", (req, res) => {
  // req > es el request del cliente
  // res > es la respuesta
  res.status(200).json({
    message: "Peticion realizada exitosamente",
  });
});
app.get("/productos", (req, res) => {
  // req > es el request del cliente
  // res > es la respuesta
  res.status(200).json({
    productos: productos,
  });
});
app.post("/producto", (req, res) => {
  //   siempre se debe envir un respuesta
  console.log(req.body);
  if (req.body) {
    productos.push(req.body);
    res.status(201).json({
      message: "Enviando la respuesta desde back: producto agregado 👍🏻",
      producto: productos,
    });
  } else {
    res.status(400).json({
      message: "Información incorrecta",
    });
  }
});

// varios métodos en una ruta
app
  .route("/producto/:id")
  .get((req, res) => {
    if (req.body) {
      const { id } = req.params;
      // const {id: nuevoId} = req.params;
      if (productos[id - 1]) {
        return res.status(200).json({
          content: productos[id - 1],
        });
      } else {
        return res.status(400).json({
          message: "Producto no existe",
          content: null,
        });
      }
    }
    // con «return» este código es inaccesible
    res.json({
      message: null,
    });
  })
  .put((req, res) => {
    const { id } = req.params;
    if (productos[id - 1]) {
      productos[id - 1] = req.body;
      return res.status(200).json({
        message: "Producto actualizado exitosamente",
        product: productos[id - 1],
      });
    } else {
      return res.status(400).json({
        message: "Producto no existe",
        content: null,
      });
    }
  })
  .delete((req, res) => {
    const { id } = req.params;
    if (productos[id - 1]) {
      productos.splice(id - 1, 1);
      return res.status(200).json({
        message: "Producto eliminado exitosamente",
      });
    } else {
      return res.status(400).json({
        message: "Producto no existe",
      });
    }
  });

//cuando se levante un servidor de express, se mantendrá escuchando las consultas realizadas mediante el puerto definido
app.listen(puerto, () => {
  console.log(`Servidor levantado exitosamente en el puerto: ${puerto}`);
});
