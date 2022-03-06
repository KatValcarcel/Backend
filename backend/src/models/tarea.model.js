import mongoose from "mongoose";

const tareaSchema = new mongoose.Schema(
  {
    nombre: {
      type: mongoose.Schema.Types.String,
      required: true,
      maxlength: 50,
    },
    status: {
      enum: ["POR_HACER", "HACIENDO", "HECHO"],
      type: mongoose.Schema.Types.String,
      required: true,
      //   maxlength: 50,
      default: "POR_HACER",
    },
    fecha_vencimiento: {
      type: mongoose.Schema.Types.Date,
      required: true,
    },

    usuarioId: {
      alias: "usuario_id",
      type: mongoose.Schema.Types.ObjectId,
      required: true,
    },
  },
  {
    //  creará las auditorías
    timestamps: true,
  }
);

export const Tarea = mongoose.model("tareas", tareaSchema);
