import { HangerIcon, HeartIcon } from '@/icons';
import { Image } from 'expo-image';
import React, { useEffect } from 'react';
import { Dimensions, StyleSheet } from 'react-native';
import Animated, {
  Easing,
  useAnimatedKeyboard,
  useAnimatedStyle,
  useSharedValue,
  withRepeat,
  withSequence,
  withTiming
} from 'react-native-reanimated';

const { width, height } = Dimensions.get('window');

// Modular grid configuration
const GRID_CONFIG = {
  baseModule: 40, // Base unit size in pixels
  spacing: 12,    // Space between modules
  get moduleSize() {
    return this.baseModule + this.spacing;
  },
  get cols() {
    return Math.ceil(width / this.moduleSize) + 2;
  },
  get rows() {
    return Math.ceil(height / this.moduleSize) + 2;
  },
  // Responsive adjustments
  getResponsiveModule() {
    const screenSize = Math.min(width, height);
    if (screenSize < 400) return 32;
    if (screenSize < 600) return 40;
    return 48;
  }
};

// Update module size based on screen size
GRID_CONFIG.baseModule = GRID_CONFIG.getResponsiveModule();

interface PatternIconProps {
  icon: string;
  row: number;
  col: number;
  delay: number;
}

function PatternIcon({ icon, row, col, delay }: PatternIconProps) {
  const opacity = useSharedValue(0);
  const scale = useSharedValue(0.5);
  const rotation = useSharedValue(0);

  useEffect(() => {
    opacity.value = withTiming(0.3, {
      duration: 800,
      easing: Easing.out(Easing.cubic),
    });

    scale.value = withSequence(
      withTiming(0.5, { duration: 0 }),
      withTiming(1, {
        duration: 800,
        easing: Easing.out(Easing.back(1.5)),
      })
    );

    rotation.value = withRepeat(
      withTiming(360, {
        duration: 8000,
        easing: Easing.linear,
      }),
      -1,
      false
    );
  }, []);

  const animatedStyle = useAnimatedStyle(() => {
    return {
      opacity: opacity.value,
      transform: [
        { scale: scale.value },
        { rotate: `${rotation.value}deg` },
      ],
    };
  });

  // Use modular grid positioning
  const x = col * GRID_CONFIG.moduleSize + GRID_CONFIG.spacing / 2;
  const y = row * GRID_CONFIG.moduleSize + GRID_CONFIG.spacing / 2;

  return (
    <Animated.View
      style={[
        styles.patternIcon,
        {
          left: x,
          top: y,
        },
        animatedStyle,
      ]}
    >
      {icon === "coat.fill" && (
        <HangerIcon
          size={32}
          color="rgba(255, 255, 255, 0.4)"
          outline={false}
        />
      )}
      {icon === "heart.fill" && (
        <HeartIcon
          size={32}
          color="rgba(255, 255, 255, 0.4)"
        />
      )}
    </Animated.View>
  );
}

interface AnimatedLogoScreenProps {
  children?: React.ReactNode;
}

export default function AnimatedLogoScreen({ children }: AnimatedLogoScreenProps) {
  const backgroundOpacity = useSharedValue(0);
  const logoScale = useSharedValue(0);
  const logoOpacity = useSharedValue(0);
  const logoTranslateY = useSharedValue(0);
  const formContainerOpacity = useSharedValue(0);
  const formContainerTranslateY = useSharedValue(0);

  // Keyboard handling
  const keyboard = useAnimatedKeyboard();

  useEffect(() => {
    // Initial animations
    backgroundOpacity.value = withTiming(1, {
      duration: 1000,
      easing: Easing.out(Easing.cubic),
    });

    setTimeout(() => {
      logoOpacity.value = withTiming(1, {
        duration: 800,
        easing: Easing.out(Easing.cubic),
      });

      logoScale.value = withSequence(
        withTiming(1.2, {
          duration: 600,
          easing: Easing.out(Easing.back(1.5)),
        }),
        withTiming(1, {
          duration: 300,
          easing: Easing.out(Easing.cubic),
        })
      );
    }, 500);

    // After logo appears, move it up and fade in the form simultaneously
    setTimeout(() => {
      logoTranslateY.value = withTiming(-120, {
        duration: 800,
        easing: Easing.out(Easing.cubic),
      });

      formContainerOpacity.value = withTiming(1, {
        duration: 800,
        easing: Easing.out(Easing.cubic),
      });
    }, 2000);
  }, []);

  const backgroundAnimatedStyle = useAnimatedStyle(() => {
    return {
      opacity: backgroundOpacity.value,
    };
  });

  const logoAnimatedStyle = useAnimatedStyle(() => {
    const keyboardOffset = keyboard.height.value > 0 ? -keyboard.height.value * 0.3 : 0;

    return {
      opacity: keyboardOffset ? 0 : logoOpacity.value,
      transform: [
        { scale: logoScale.value },
        { translateY: logoTranslateY.value }
      ],
    };
  });

  const formContainerAnimatedStyle = useAnimatedStyle(() => {
    return {
      opacity: formContainerOpacity.value,
      transform: [
        { translateY: formContainerTranslateY.value },
        { translateY: -keyboard.height.value * 0.7 }
      ],
    };
  });

  const containerAnimatedStyle = useAnimatedStyle(() => {
    return {
      paddingBottom: keyboard.height.value > 0 ? keyboard.height.value * 0.2 : 0,
    };
  });

  const generatePattern = () => {
    const icons = [];
    const { rows, cols } = GRID_CONFIG;

    for (let row = 0; row < rows; row++) {
      for (let col = 0; col < cols; col++) {
        const rowInPattern = row % 4; // 4-row repeating pattern
        let icon = 'heart.fill';
        let shouldRender = true;

        switch (rowInPattern) {
          case 0: // Row 1: Hearts from start to end
            icon = 'heart.fill';
            if (col % 2 !== 0) {
              shouldRender = false;
            }
            break;
          case 1: // Row 2: Hangers directly below hearts
            icon = 'coat.fill';
            if (col % 2 !== 0) {
              shouldRender = false;
            }
            break;
          case 2: // Row 3: Hearts offset by half position (between hangers)
            icon = 'heart.fill';
            // Offset by half - skip every other column starting from 0
            if (col % 2 === 0) {
              shouldRender = false;
            }
            break;
          case 3: // Row 4: Hangers directly below hearts of row 3
            icon = 'coat.fill';
            // Only render where hearts were in row 3 (odd columns)
            if (col % 2 === 0) {
              shouldRender = false;
            }
            break;
        }

        if (shouldRender) {
          const delay = (row + col) * 0.05; // Adjusted timing for smoother animation
          icons.push(
            <PatternIcon
              key={`${row}-${col}`}
              icon={icon}
              row={row}
              col={col}
              delay={delay}
            />
          );
        }
      }
    }

    return icons;
  };

  return (
    <Animated.View style={[styles.container, containerAnimatedStyle]}>
      <Animated.View style={[styles.background, backgroundAnimatedStyle]}>
        {generatePattern()}
      </Animated.View>

      <Animated.View style={[styles.logoContainer, logoAnimatedStyle]}>
        <Image
          source={require('@/assets/images/logo.png')}
          style={styles.logo}
          contentFit="contain"
        />
      </Animated.View>

      <Animated.View style={[styles.formContainer, formContainerAnimatedStyle]}>
        {children}
      </Animated.View>
    </Animated.View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#FF33A3',
  },
  background: {
    ...StyleSheet.absoluteFillObject,
    backgroundColor: '#FF33A3',
  },
  patternIcon: {
    position: 'absolute',
    width: GRID_CONFIG.baseModule,
    height: GRID_CONFIG.baseModule,
    justifyContent: 'center',
    alignItems: 'center',
  },
  logoContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  logo: {
    width: 120,
    height: 120,
  },
  formContainer: {
    position: 'absolute',
    bottom: 0,
    left: 0,
    right: 0,
    height: 300,
    justifyContent: 'flex-end',
    paddingHorizontal: 20,
    paddingBottom: 40,
  },
  formPlaceholder: {
    backgroundColor: '#FEF8EB',
    borderRadius: 20,
    padding: 20,
    minHeight: 200,
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: -2,
    },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 5,
  },
});