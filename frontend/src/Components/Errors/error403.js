import { Result, Button } from 'antd';

export const error403 = () => {
    <Result
    status="403"
    title="403"
    subTitle="Sorry, you are not authorized to access this page."
    extra={<Button type="primary">Back Home</Button>}
  />
}
 
