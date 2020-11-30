import {Menu} from 'antd'
import { Link } from 'react-router-dom'
export function MenuComponent(){
    return (
    <Menu theme="dark" mode="horizontal">
        
        <Menu.Item key="1">
            <Link to="/">
                Home
            </Link>
        </Menu.Item>

        <Menu.Item key="2">
            <Link to="/login">
                Login
            </Link>
        </Menu.Item>

        <Menu.Item key="3">
            <Link to="signup">
                Signup    
            </Link>
        </Menu.Item>
    </Menu>
    )

}
