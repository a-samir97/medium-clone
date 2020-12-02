import { message, Button, Space } from 'antd';

// i think this is factory design pattern :D 

export const messageHandler = (type, content) => {

    if (type === "sucess"){
        return message.success(content)

    } else if (type === "error") {
        return message.error(content)

    } else if (type === "warning"){ 
        return message.warning(content)
    
    } else if (type === "info"){
        return message.info(content)
    }
}

