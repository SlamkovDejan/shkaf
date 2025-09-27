import { Colors } from '@/constants/theme';
import React, { useState } from 'react';
import { StyleSheet, Text, TextInput, View } from 'react-native';

interface TextInputFieldProps {
  label?: string;
  placeholder?: string;
  value?: string;
  onChangeText?: (text: string) => void;
  error?: string;
  secureTextEntry?: boolean;
  keyboardType?: 'default' | 'email-address' | 'numeric' | 'phone-pad';
  autoCapitalize?: 'none' | 'sentences' | 'words' | 'characters';
  style?: any;
}

export default function TextInputField({
  label,
  placeholder,
  value,
  onChangeText,
  error,
  secureTextEntry = false,
  keyboardType = 'default',
  autoCapitalize = 'sentences',
  style,
}: TextInputFieldProps) {
  const [isFocused, setIsFocused] = useState(false);

  const getInputState = () => {
    if (error) return 'error';
    if (isFocused) return 'active';
    return 'normal';
  };

  const inputState = getInputState();

  return (
    <View style={[styles.container, style]}>
      {label && (
        <Text style={[
          styles.label,
          inputState === 'error' && styles.labelError,
          inputState === 'active' && styles.labelActive,
        ]}>
          {label}
        </Text>
      )}

      <TextInput
        style={[
          styles.input,
          inputState === 'normal' && styles.inputNormal,
          inputState === 'active' && styles.inputActive,
          inputState === 'error' && styles.inputError,
        ]}
        placeholder={placeholder}
        placeholderTextColor={
          inputState === 'error' ? Colors.light.error :
          inputState === 'active' ? Colors.light.primary :
          Colors.light.placeholder
        }
        value={value}
        onChangeText={onChangeText}
        onFocus={() => setIsFocused(true)}
        onBlur={() => setIsFocused(false)}
        secureTextEntry={secureTextEntry}
        keyboardType={keyboardType}
        autoCapitalize={autoCapitalize}
      />

      {error && (
        <Text style={styles.errorText}>
          {error}
        </Text>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    marginBottom: 16,
  },
  label: {
    fontSize: 16,
    fontWeight: '600',
    marginBottom: 8,
    color: Colors.light.text,
  },
  labelActive: {
    color: Colors.light.primary,
  },
  labelError: {
    color: Colors.light.error,
  },
  input: {
    height: 50,
    borderRadius: 12,
    paddingHorizontal: 16,
    fontSize: 16,
    backgroundColor: Colors.light.background,
    borderWidth: 1,
    borderBottomWidth: 3,
  },
  inputNormal: {
    borderColor: Colors.light.text,
  },
  inputActive: {
    borderColor: Colors.light.primary,
    shadowColor: Colors.light.primary,
    shadowOffset: {
      width: 0,
      height: 0,
    },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 2,
  },
  inputError: {
    borderColor: Colors.light.error,
  },
  errorText: {
    fontSize: 14,
    color: Colors.light.error,
    marginTop: 6,
    marginLeft: 4,
  },
});