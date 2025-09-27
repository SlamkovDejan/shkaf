import AnimatedLogoScreen from '@/components/animated-logo-screen';
import TextInputField from '@/components/ui/text-input';
import { Colors } from '@/constants/theme';
import React, { useState } from 'react';
import { StyleSheet, Text, TouchableOpacity, View } from 'react-native';

export default function LoginScreen() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [emailError, setEmailError] = useState('');
  const [passwordError, setPasswordError] = useState('');

  const validateEmail = (email: string) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  };

  const handleLogin = () => {
    let hasError = false;

    // Reset errors
    setEmailError('');
    setPasswordError('');

    // Validate email
    if (!email) {
      setEmailError('Email адреса е задолжителна');
      hasError = true;
    } else if (!validateEmail(email)) {
      setEmailError('Внесете валидна email адреса');
      hasError = true;
    }

    // Validate password
    if (!password) {
      setPasswordError('Лозинката е задолжителна');
      hasError = true;
    } else if (password.length < 6) {
      setPasswordError('Лозинката мора да има најмалку 6 карактери');
      hasError = true;
    }

    if (!hasError) {
      // Handle successful login
      console.log('Login attempt:', { email, password });
    }
  };

  const renderForm = () => (
    <View
      style={styles.formContainer}
    >
      <View style={styles.form}>
        <TextInputField
          label="Email адреса"
          placeholder="Email"
          value={email}
          onChangeText={(text) => {
            setEmail(text);
            if (emailError) setEmailError('');
          }}
          error={emailError}
          keyboardType="email-address"
          autoCapitalize="none"
        />

        <TextInputField
          label="Лозинка"
          placeholder="Лозинка"
          value={password}
          onChangeText={(text) => {
            setPassword(text);
            if (passwordError) setPasswordError('');
          }}
          error={passwordError}
          secureTextEntry
        />

        <TouchableOpacity style={styles.loginButton} onPress={handleLogin}>
          <Text style={styles.loginButtonText}>Најави се</Text>
        </TouchableOpacity>

        <View style={styles.signupContainer}>
          <Text style={styles.signupText}>Не си корисник? </Text>
          <TouchableOpacity>
            <Text style={styles.signupLink}>Регистрирај се тука</Text>
          </TouchableOpacity>
        </View>
      </View>
    </View>
  );

  return (
    <AnimatedLogoScreen>
      {renderForm()}
    </AnimatedLogoScreen>
  );
}

const styles = StyleSheet.create({
  formContainer: {
    flex: 1,
    justifyContent: 'flex-end',
  },
  form: {
    backgroundColor: Colors.light.background,
    borderRadius: 20,
    padding: 24,
    marginHorizontal: 5,
    marginBottom: 40,
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: -2,
    },
    shadowOpacity: 0.1,
    shadowRadius: 12,
    elevation: 8,
  },
  loginButton: {
    backgroundColor: "#4000FF",
    borderRadius: 38,
    height: 50,
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: 8,
    shadowColor: '#3400CF',
    shadowOffset: {
      width: 0,
      height: 4,
    },
    shadowOpacity: 0.3,
    shadowRadius: 8,
    elevation: 4,
  },
  loginButtonText: {
    color: Colors.light.background,
    fontSize: 16,
    fontWeight: '600',
  },
  signupContainer: {
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: 20,
  },
  signupText: {
    fontSize: 16,
    color: Colors.light.text,
  },
  signupLink: {
    fontSize: 16,
    color: '#4000FF',
    fontWeight: '600',
    textDecorationLine: 'underline',
  },
});