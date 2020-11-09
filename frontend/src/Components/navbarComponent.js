import {Menu} from 'antd'

export function MenuComponent(){
    return (
    <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['2']}>
        <Menu.Item key="1">Home</Menu.Item>
        <Menu.Item key="2">Profile</Menu.Item>
        <Menu.Item key="3">nav 3</Menu.Item>
    </Menu>
    )

}
