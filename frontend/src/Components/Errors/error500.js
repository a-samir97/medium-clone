import { Result, Button } from 'antd';

export const error500 = () => {
    <Result
    status="500"
    title="500"
    subTitle="Sorry, something went wrong."
    extra={<Button type="primary">Back Home</Button>}
  />
}
