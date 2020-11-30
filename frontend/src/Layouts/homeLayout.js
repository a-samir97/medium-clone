import { Component } from 'react';
import { MenuComponent } from '../Components/Navbar/navbarComponent'
import { Layout, Menu } from 'antd';
import { UserOutlined, LaptopOutlined } from '@ant-design/icons';

const { SubMenu } = Menu;
const { Header, Content, Sider } = Layout;


export class HomeLayout extends Component {
    render(){
        return (

    <Layout>
    <Layout>
      <Sider width={200} className="site-layout-background">
        <Menu
          mode="inline"
          defaultSelectedKeys={['1']}
          defaultOpenKeys={['sub1']}
          style={{ height: '100%', borderRight: 0 }}
        >
          <SubMenu key="sub1" icon={<LaptopOutlined />} title="Blogs">
            <Menu.Item key="1">First Blog</Menu.Item>
            <Menu.Item key="2">Second Blog</Menu.Item>
            <Menu.Item key="3">Third Blog</Menu.Item>
            <Menu.Item key="4">Forth Blog</Menu.Item>
          </SubMenu>
        </Menu>
      </Sider>
      <Layout style={{ padding: '0 24px 24px' }}>
        <Content
          className="site-layout-background"
          style={{
            padding: 24,
            margin: 0,
            minHeight: 280,
          }}
        >
          Content
        </Content>
      </Layout>
    </Layout>
  </Layout>
        )
    }
}
