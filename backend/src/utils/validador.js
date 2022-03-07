import jwt from "jsonwebtoken";

const verificarToken = (token) => {
  try {
    const payload = jwt.verify(token, process.env.SECRET_JWT);
    return payload;
  } catch (error) {
    if (error instanceof Error) {
      return error.message;
    }
  }
};

export const validarUsuario = (req, res, next) => {
  if (!req.headers.authorization) {
    return res.status(401).json({
      message: "Este request necesita una token",
    });
  }
  const token = req.headers.authorization.split(" ")[1];
  const resultado = verificarToken(token);

  if (typeof resultado === "object") {
    const { id } = resultado;
    req.user = id;
    next();
  } else {
    return res.status(401).json({
      message: "Error al hacer la petición",
      content: resultado,
    });
  }
};
// averiguar blacklist de las TOKENS
