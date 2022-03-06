import mongoose from "mongoose";
import { hashSync } from "bcrypt";

const usuarioSchema = new mongoose.Schema(
  {
    correo: {
      type: mongoose.Schema.Types.String,
      required: true,
      unique: true,
      maxlength: 50,
    },
    password: {
      type: mongoose.Schema.Types.String,
      required: true,
      set: (valor) => {
        // encriptacion de la contraseña
        // el set se llamara cuando vayamos a agregar o actualizar un registro en la bd y antes de que sea guardado
        const cryptPass = hashSync(valor, 10);
        return cryptPass;
      },
    },
    nombre: {
      type: mongoose.Schema.Types.String,
      required: true,
      maxlength: 50,
    },
    apellido: {
      type: mongoose.Schema.Types.String,
      required: true,
      maxlength: 50,
    },
    pais: {
      enum: [
        "BRAZIL",
        "COLOMBIA",
        "PERU",
        "CHILE",
        "URUGUAY",
        "ARGENTINA",
        "PARAGUAY",
        "BOLIVIA",
        "ECUADOR",
        "GUYANA FRANCESA",
        "VENEZUELA",
        "SURINAM",
      ],
      type: mongoose.Schema.Types.String,
      required: true,
    },
  },
  {
    //  creará las auditorías
    timestamps: true,
  }
);

export const Usuario = mongoose.model("usuarios", usuarioSchema);
