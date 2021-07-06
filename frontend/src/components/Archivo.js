import React from "react";
import "./Archivo.css";

export const Archivo = ({ texto, onDrop }) => {
  return (
    <div
      className="area"
      onDragOver={(e) => e.preventDefault()}
      onDrop={onDrop}
    >
      <h5>{texto}</h5>
    </div>
  );
};
