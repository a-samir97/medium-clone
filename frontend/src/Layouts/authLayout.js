import { RegistrationForm } from '../Components/Auth/signupComponent';
import { LoginComponent } from '../Components/Auth/loginComponents';
import {Row, Col} from 'antd'
export const AuthLayout = () => {
    return (
        <Row>
            <Col span={12}>
                <RegistrationForm></RegistrationForm>
            </Col>
            <Col span={12}>
                <LoginComponent></LoginComponent>
            </Col>
        </Row>    
    )
}
