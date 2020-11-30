import { 
  Form, 
  Input, 
  Button, 
  Checkbox, 
} from 'antd';

import axiosInstance from '../../Api/axiosAPI'

const layout = {
  labelCol: {
    span: 8,
  },
  wrapperCol: {
    span: 8,
  },
};

const tailLayout = {
  wrapperCol: {
    offset: 8,
    span: 16,
  },
};

export const LoginComponent = () => {

  const onFinish = (values) => {
      const response = axiosInstance.post('/token/obtain/', {
        username:values.username,
        password:values.password
      }).then(result => {
        axiosInstance.defaults.headers['Authorization'] = "JWT " + result.data.access;
        localStorage.setItem('access_token', result.data.access)
        localStorage.setItem('refresh_token', result.data.refresh)
      }).catch(error => {
        throw error
      })
 
  };

  const onFinishFailed = (errorInfo) => {
    console.log('Failed:', errorInfo);
  };

  return (

    <Form
      {...layout}
      name="basic"
      initialValues={{
        remember: true,
      }}
      onFinish={onFinish}
      onFinishFailed={onFinishFailed}
      style={{marginTop:10}}
    >
      <Form.Item
        label="Username"
        name="username"
        rules={[
          {
            required: true,
            message: 'Please input your username!',
          },
        ]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        label="Password"
        name="password"
        rules={[
          {
            required: true,
            message: 'Please input your password!',
          },
        ]}
      >
        <Input.Password />
      </Form.Item>

      <Form.Item {...tailLayout} name="remember" valuePropName="checked">
        <Checkbox>Remember me</Checkbox>
      </Form.Item>

      <Form.Item {...tailLayout}>
        <Button type="primary" htmlType="submit">
          Submit
        </Button>
      </Form.Item>
    </Form>
  );
};
