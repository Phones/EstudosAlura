import "./InputText.css";

const InputText = () => {
    return (
        <div className="input-text">
            <label>Nome</label>
            <input placeholder="Digite o seu nome" type="text" />
        </div>
    );
}

export default InputText;