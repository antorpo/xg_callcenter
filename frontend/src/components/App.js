import React, { useState } from "react";
import "./App.css";
import "../css/style.css";
import logo from "../images/logo.png";
import { Button, Table } from "react-bootstrap";
import { Archivo } from "./Archivo";
import { Loader } from "./Loader";
import { default as textos } from "./strings.json";
import { useAlert } from "react-alert";
import axios from "axios";
import Rating from "@material-ui/lab/Rating";

const App = (props) => {
  const alert = useAlert();
  const [cadena, setCadena] = useState({
    secuencia: "",
  });
  const [tokens, setTokens] = useState({
    loading: false,
    error: null,
    data: [],
  });
  const [archivo, setArchivo] = useState(null);
  const [textoA, setTextoA] = useState(textos.archivo);

  const createCadena = () => {
    if (cadena.secuencia) {
      axios.post(`/api/cadena-create/`, cadena).then((res) => {
        getTokens();
        alert.success(textos.exito_cadena);
      });
    } else {
      alert.error(textos.error_cadena);
      setTokens({
        loading: false,
        data: [],
        error: null,
      });
    }
  };

  const getTokens = () => {
    setTokens({
      loading: true,
      error: null,
    });

    try {
      axios.get(`/api/historial/`).then((res) => {
        const tokens = res.data;
        setTokens({
          loading: false,
          data: tokens,
        });

        deleteCadena();
      });
    } catch (error) {
      setTokens({
        loading: false,
        error: error,
      });
    }
  };

  const deleteCadena = () => {
    axios.delete(`/api/cadena-delete-all/`).then((res) => {
      console.log(res.data);
    });
  };

  const handleDrop = (e) => {
    e.preventDefault();

    let archivoT = e.dataTransfer.files[0];

    if (archivoT.type === "text/plain") {
      let reader = new FileReader();
      reader.onloadend = () => {
        setCadena({
          secuencia: reader.result,
        });
      };
      reader.readAsText(archivoT);
      setTextoA(archivoT.name);
      setArchivo(archivoT);
    } else {
      alert.error(textos.alertas.error);
      setArchivo(null);
      setTextoA(textos.archivo);
      setCadena({
        secuencia: "",
      });
    }
  };

  return (
    <div id="recuadro">
      <div id="logo">
        <img src={logo} width="20%" />
      </div>
      <h1>{textos.titulo}</h1>
      <br />
      <h5 id="nombres">{textos.nombres}</h5>
      <div className="container centrar">
        <Archivo texto={textoA} onDrop={handleDrop} />
        <Button
          variant={archivo ? "success" : "secondary"}
          className="boton_enviar"
          onClick={createCadena}
          disabled={!archivo}
        >
          {textos.boton}
        </Button>

        <div className="container espaciado_abajo">
          {tokens.loading && (
            <div className="text-center">
              <Loader mensaje={textos.cargando} />
            </div>
          )}

          {!tokens.loading && tokens.data.length !== 0 && archivo && (
            <>
              <h4 className="fw-bold border border-secondary fondo_blanco">
                {textos.reporte}
              </h4>
              <Table striped bordered hover className="fondo_blanco">
                <thead>
                  <tr>
                    <th>CONVERSACIÓN</th>
                    <th>PUNTAJE</th>
                    <th>CALIFICACIÓN</th>
                  </tr>
                </thead>
                <tbody>
                  {tokens.data.map((token, index) => (
                    <tr key={index}>
                      <td>{token[0]}</td>
                      <td>{token[1]}</td>
                      <td>
                        <Rating name="disabled" value={token[2]} disabled />
                      </td>
                    </tr>
                  ))}
                </tbody>
              </Table>
            </>
          )}
        </div>
      </div>
    </div>
  );
};

export default App;
