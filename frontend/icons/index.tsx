import React from 'react';
import Svg, { Path } from 'react-native-svg';

interface HeartIconProps {
	size?: number;
	color?: string;
}

export const HeartIcon = ({ size = 24, color = '#FEF8EB' }: HeartIconProps) => (
	<Svg
		width={size}
		height={size}
		fill="none"
		viewBox="0 0 18 18"
		style={{ width: size, height: size }}
	>
		<Path
			d="M3.99686 10.6084H5.4223V12.2116H6.85712V13.8254H8.28257V15.4286H9.70802V13.8254H11.1428V12.2116H12.5683V10.6084H14.0031V8.99471H15.4286V4.1746H14.0031V2.57141H9.70802V4.1746H8.28257V2.57141H3.99686V4.1746H2.57141V8.99471H3.99686V10.6084Z"
			fill={color}
		/>
	</Svg>
);

export const HangerIcon = ({ size = 24, color = '#FEF8EB', outline = false }) => (
	<Svg
		width={size}
		height={size}
		viewBox="0 0 100 100"
		fill="none"
		style={{ width: size, height: size }}
	>
		<Path d="M49.9963 13.1979H46.4904V16.7037H49.9963V13.1979Z" fill={color} />
		<Path d="M53.5022 13.1979H49.9963V16.7037H53.5022V13.1979Z" fill={color} />
		<Path d="M57.008 13.1979H53.5022V16.7037H57.008V13.1979Z" fill={color} />
		<Path d="M60.5139 13.1979H57.008V16.7037H60.5139V13.1979Z" fill={color} />
		<Path d="M46.4904 16.7037H42.9846V20.2096H46.4904V16.7037Z" fill={color} />
		<Path d="M49.9963 16.7037H46.4904V20.2096H49.9963V16.7037Z" fill={color} />
		<Path d="M53.5022 16.7037H49.9963V20.2096H53.5022V16.7037Z" fill={color} />
		<Path d="M57.008 16.7037H53.5022V20.2096H57.008V16.7037Z" fill={color} />
		<Path d="M60.5139 16.7037H57.008V20.2096H60.5139V16.7037Z" fill={color} />
		<Path d="M64.0197 16.7037H60.5139V20.2096H64.0197V16.7037Z" fill={color} />
		<Path d="M42.9846 20.2096H39.4787V23.7155H42.9846V20.2096Z" fill={color} />
		<Path d="M46.4904 20.2096H42.9846V23.7155H46.4904V20.2096Z" fill={color} />
		<Path d="M49.9963 20.2096H46.4904V23.7155H49.9963V20.2096Z" fill={color} />
		<Path d="M60.5139 20.2096H57.008V23.7155H60.5139V20.2096Z" fill={color} />
		<Path d="M64.0197 20.2096H60.5139V23.7155H64.0197V20.2096Z" fill={color} />
		<Path d="M67.5256 20.2096H64.0197V23.7155H67.5256V20.2096Z" fill={color} />
		<Path d="M42.9846 23.7155H39.4787V27.2213H42.9846V23.7155Z" fill={color} />
		<Path d="M46.4904 23.7155H42.9846V27.2213H46.4904V23.7155Z" fill={color} />
		<Path d="M64.0197 23.7155H60.5139V27.2213H64.0197V23.7155Z" fill={color} />
		<Path d="M67.5256 23.7155H64.0197V27.2213H67.5256V23.7155Z" fill={color} />
		<Path d="M64.0197 27.2213H60.5139V30.7272H64.0197V27.2213Z" fill={color} />
		<Path d="M67.5256 27.2213H64.0197V30.7272H67.5256V27.2213Z" fill={color} />
		<Path d="M60.5139 30.7272H57.008V34.233H60.5139V30.7272Z" fill={color} />
		<Path d="M64.0197 30.7272H60.5139V34.233H64.0197V30.7272Z" fill={color} />
		<Path d="M67.5256 30.7272H64.0197V34.233H67.5256V30.7272Z" fill={color} />
		<Path d="M49.9963 34.233H46.4904V37.7389H49.9963V34.233Z" fill={color} />
		<Path d="M53.5022 34.233H49.9963V37.7389H53.5022V34.233Z" fill={color} />
		<Path d="M57.008 34.233H53.5022V37.7389H57.008V34.233Z" fill={color} />
		<Path d="M60.5139 34.233H57.008V37.7389H60.5139V34.233Z" fill={color} />
		<Path d="M64.0197 34.233H60.5139V37.7389H64.0197V34.233Z" fill={color} />
		<Path d="M49.9963 37.7389H46.4904V41.2448H49.9963V37.7389Z" fill={color} />
		<Path d="M53.5022 37.7389H49.9963V41.2448H53.5022V37.7389Z" fill={color} />
		<Path d="M57.008 37.7389H53.5022V41.2448H57.008V37.7389Z" fill={color} />
		<Path d="M60.5139 37.7389H57.008V41.2448H60.5139V37.7389Z" fill={color} />
		<Path d="M49.9963 41.2448H46.4904V44.7506H49.9963V41.2448Z" fill={color} />
		<Path d="M53.5022 41.2448H49.9963V44.7506H53.5022V41.2448Z" fill={color} />
		<Path d="M49.9963 44.7506H46.4904V48.2565H49.9963V44.7506Z" fill={color} />
		<Path d="M53.5022 44.7506H49.9963V48.2565H53.5022V44.7506Z" fill={color} />
		<Path d="M39.4787 48.2565H35.9729V51.7623H39.4787V48.2565Z" fill={color} />
		<Path d="M42.9846 48.2565H39.4787V51.7623H42.9846V48.2565Z" fill={color} />
		<Path d="M46.4904 48.2565H42.9846V51.7623H46.4904V48.2565Z" fill={color} />
		<Path d="M49.9963 48.2565H46.4904V51.7623H49.9963V48.2565Z" fill={color} />
		<Path d="M53.5022 48.2565H49.9963V51.7623H53.5022V48.2565Z" fill={color} />
		<Path d="M57.008 48.2565H53.5022V51.7623H57.008V48.2565Z" fill={color} />
		<Path d="M60.5139 48.2565H57.008V51.7623H60.5139V48.2565Z" fill={color} />
		<Path d="M64.0197 48.2565H60.5139V51.7623H64.0197V48.2565Z" fill={color} />
		<Path d="M35.9729 51.7623H32.467V55.2682H35.9729V51.7623Z" fill={color} />
		<Path d="M39.4787 51.7623H35.9729V55.2682H39.4787V51.7623Z" fill={color} />
		<Path d="M42.9846 51.7623H39.4787V55.2682H42.9846V51.7623Z" fill={color} />
		<Path d="M46.4904 51.7623H42.9846V55.2682H46.4904V51.7623Z" fill={color} />
		<Path d="M49.9963 51.7623H46.4904V55.2682H49.9963V51.7623Z" fill={color} />
		<Path d="M53.5022 51.7623H49.9963V55.2682H53.5022V51.7623Z" fill={color} />
		<Path d="M57.008 51.7623H53.5022V55.2682H57.008V51.7623Z" fill={color} />
		<Path d="M60.5139 51.7623H57.008V55.2682H60.5139V51.7623Z" fill={color} />
		<Path d="M64.0197 51.7623H60.5139V55.2682H64.0197V51.7623Z" fill={color} />
		<Path d="M67.5256 51.7623H64.0197V55.2682H67.5256V51.7623Z" fill={color} />
		<Path d="M32.467 55.2682H28.9612V58.7741H32.467V55.2682Z" fill={color} />
		<Path d="M35.9729 55.2682H32.467V58.7741H35.9729V55.2682Z" fill={color} />
		<Path d="M39.4787 55.2682H35.9729V58.7741H39.4787V55.2682Z" fill={color} />
		<Path d="M42.9846 55.2682H39.4787V58.7741H42.9846V55.2682Z" fill={color} />
		<Path d="M46.4904 55.2682H42.9846V58.7741H46.4904V55.2682Z" fill={color} />
		<Path d="M49.9963 55.2682H46.4904V58.7741H49.9963V55.2682Z" fill={color} />
		<Path d="M53.5022 55.2682H49.9963V58.7741H53.5022V55.2682Z" fill={color} />
		<Path d="M57.008 55.2682H53.5022V58.7741H57.008V55.2682Z" fill={color} />
		<Path d="M60.5139 55.2682H57.008V58.7741H60.5139V55.2682Z" fill={color} />
		<Path d="M64.0197 55.2682H60.5139V58.7741H64.0197V55.2682Z" fill={color} />
		<Path d="M67.5256 55.2682H64.0197V58.7741H67.5256V55.2682Z" fill={color} />
		<Path d="M71.0314 55.2682H67.5256V58.7741H71.0314V55.2682Z" fill={color} />
		<Path d="M28.9612 58.7741H25.4553V62.2799H28.9612V58.7741Z" fill={color} />
		<Path d="M32.467 58.7741H28.9612V62.2799H32.467V58.7741Z" fill={color} />
		<Path d="M35.9729 58.7741H32.467V62.2799H35.9729V58.7741Z" fill={color} />
		<Path d="M39.4787 58.7741H35.9729V62.2799H39.4787V58.7741Z" fill={color} />
		<Path d="M42.9846 58.7741H39.4787V62.2799H42.9846V58.7741Z" fill={color} />
		<Path d="M60.5139 58.7741H57.008V62.2799H60.5139V58.7741Z" fill={color} />
		<Path d="M64.0197 58.7741H60.5139V62.2799H64.0197V58.7741Z" fill={color} />
		<Path d="M67.5256 58.7741H64.0197V62.2799H67.5256V58.7741Z" fill={color} />
		<Path d="M71.0314 58.7741H67.5256V62.2799H71.0314V58.7741Z" fill={color} />
		<Path d="M74.5373 58.7741H71.0314V62.2799H74.5373V58.7741Z" fill={color} />
		<Path d="M25.4553 62.2799H21.9494V65.7858H25.4553V62.2799Z" fill={color} />
		<Path d="M28.9612 62.2799H25.4553V65.7858H28.9612V62.2799Z" fill={color} />
		<Path d="M32.467 62.2799H28.9612V65.7858H32.467V62.2799Z" fill={color} />
		<Path d="M35.9729 62.2799H32.467V65.7858H35.9729V62.2799Z" fill={color} />
		<Path d="M39.4787 62.2799H35.9729V65.7858H39.4787V62.2799Z" fill={color} />
		<Path d="M64.0197 62.2799H60.5139V65.7858H64.0197V62.2799Z" fill={color} />
		<Path d="M67.5256 62.2799H64.0197V65.7858H67.5256V62.2799Z" fill={color} />
		<Path d="M71.0314 62.2799H67.5256V65.7858H71.0314V62.2799Z" fill={color} />
		<Path d="M74.5373 62.2799H71.0314V65.7858H74.5373V62.2799Z" fill={color} />
		<Path d="M78.0432 62.2799H74.5373V65.7858H78.0432V62.2799Z" fill={color} />
		<Path d="M21.9494 65.7858H18.4436V69.2916H21.9494V65.7858Z" fill={color} />
		<Path d="M25.4553 65.7858H21.9494V69.2916H25.4553V65.7858Z" fill={color} />
		<Path d="M28.9612 65.7858H25.4553V69.2916H28.9612V65.7858Z" fill={color} />
		<Path d="M32.467 65.7858H28.9612V69.2916H32.467V65.7858Z" fill={color} />
		<Path d="M35.9729 65.7858H32.467V69.2916H35.9729V65.7858Z" fill={color} />
		<Path d="M67.5256 65.7858H64.0197V69.2916H67.5256V65.7858Z" fill={color} />
		<Path d="M71.0314 65.7858H67.5256V69.2916H71.0314V65.7858Z" fill={color} />
		<Path d="M74.5373 65.7858H71.0314V69.2916H74.5373V65.7858Z" fill={color} />
		<Path d="M78.0432 65.7858H74.5373V69.2916H78.0432V65.7858Z" fill={color} />
		<Path d="M81.549 65.7858H78.0432V69.2916H81.549V65.7858Z" fill={color} />
		<Path d="M18.4436 69.2916H14.9377V72.7975H18.4436V69.2916Z" fill={color} />
		<Path d="M21.9494 69.2916H18.4436V72.7975H21.9494V69.2916Z" fill={color} />
		<Path d="M25.4553 69.2916H21.9494V72.7975H25.4553V69.2916Z" fill={color} />
		<Path d="M28.9612 69.2916H25.4553V72.7975H28.9612V69.2916Z" fill={color} />
		<Path d="M32.467 69.2916H28.9612V72.7975H32.467V69.2916Z" fill={color} />
		<Path d="M71.0314 69.2916H67.5256V72.7975H71.0314V69.2916Z" fill={color} />
		<Path d="M74.5373 69.2916H71.0314V72.7975H74.5373V69.2916Z" fill={color} />
		<Path d="M78.0432 69.2916H74.5373V72.7975H78.0432V69.2916Z" fill={color} />
		<Path d="M81.549 69.2916H78.0432V72.7975H81.549V69.2916Z" fill={color} />
		<Path d="M85.0549 69.2916H81.549V72.7975H85.0549V69.2916Z" fill={color} />
		<Path d="M14.9377 72.7975H11.4318V76.3033H14.9377V72.7975Z" fill={color} />
		<Path d="M18.4436 72.7975H14.9377V76.3033H18.4436V72.7975Z" fill={color} />
		<Path d="M21.9494 72.7975H18.4436V76.3033H21.9494V72.7975Z" fill={color} />
		<Path d="M25.4553 72.7975H21.9494V76.3033H25.4553V72.7975Z" fill={color} />
		<Path d="M28.9612 72.7975H25.4553V76.3033H28.9612V72.7975Z" fill={color} />
		<Path d="M74.5373 72.7975H71.0314V76.3033H74.5373V72.7975Z" fill={color} />
		<Path d="M78.0432 72.7975H74.5373V76.3033H78.0432V72.7975Z" fill={color} />
		<Path d="M81.549 72.7975H78.0432V76.3033H81.549V72.7975Z" fill={color} />
		<Path d="M85.0549 72.7975H81.549V76.3033H85.0549V72.7975Z" fill={color} />
		<Path d="M88.5608 72.7975H85.0549V76.3033H88.5608V72.7975Z" fill={color} />
		<Path d="M11.4318 76.3033H7.92599V79.8092H11.4318V76.3033Z" fill={color} />
		<Path d="M14.9377 76.3033H11.4318V79.8092H14.9377V76.3033Z" fill={color} />
		<Path d="M18.4436 76.3033H14.9377V79.8092H18.4436V76.3033Z" fill={color} />
		<Path d="M21.9494 76.3033H18.4436V79.8092H21.9494V76.3033Z" fill={color} />
		<Path d="M25.4553 76.3033H21.9494V79.8092H25.4553V76.3033Z" fill={color} />
		<Path d="M78.0432 76.3033H74.5373V79.8092H78.0432V76.3033Z" fill={color} />
		<Path d="M81.549 76.3033H78.0432V79.8092H81.549V76.3033Z" fill={color} />
		<Path d="M85.0549 76.3033H81.549V79.8092H85.0549V76.3033Z" fill={color} />
		<Path d="M88.5608 76.3033H85.0549V79.8092H88.5608V76.3033Z" fill={color} />
		<Path d="M92.0666 76.3033H88.5608V79.8092H92.0666V76.3033Z" fill={color} />
		<Path d="M11.4318 79.8092H7.92599V83.3151H11.4318V79.8092Z" fill={color} />
		<Path d="M14.9377 79.8092H11.4318V83.3151H14.9377V79.8092Z" fill={color} />
		<Path d="M18.4436 79.8092H14.9377V83.3151H18.4436V79.8092Z" fill={color} />
		<Path d="M21.9494 79.8092H18.4436V83.3151H21.9494V79.8092Z" fill={color} />
		<Path d="M81.549 79.8092H78.0432V83.3151H81.549V79.8092Z" fill={color} />
		<Path d="M85.0549 79.8092H81.549V83.3151H85.0549V79.8092Z" fill={color} />
		<Path d="M88.5608 79.8092H85.0549V83.3151H88.5608V79.8092Z" fill={color} />
		<Path d="M92.0666 79.8092H88.5608V83.3151H92.0666V79.8092Z" fill={color} />
		<Path d="M11.4318 83.3151H7.92599L7.92199 86.7922H11.4278L11.4318 83.3151Z" fill={color} />
		<Path d="M14.9377 83.3151H11.4318L11.4278 86.7922H14.9337L14.9377 83.3151Z" fill={color} />
		<Path d="M18.4436 83.3151H14.9377L14.9337 86.7922L18.4436 86.8209V83.3151Z" fill={color} />
		<Path d="M85.0549 83.3151H81.549V86.8209H85.0549V83.3151Z" fill={color} />
		<Path d="M88.5608 83.3151H85.0549V86.8209H88.5608V83.3151Z" fill={color} />
		<Path d="M92.0666 83.3151H88.5608V86.8209H92.0666V83.3151Z" fill={color} />
		<Path d="M39.4787 44.7506H35.9729V48.2565H39.4787V44.7506Z" fill={outline ? "black" : undefined} />
		<Path d="M42.9846 44.7506H39.4787V48.2565H42.9846L42.9846 44.7506Z" fill={outline ? "black" : undefined} />
		<Path d="M46.4904 44.7506H42.9846L42.9846 48.2565H46.4904V44.7506Z" fill={outline ? "black" : undefined} />
		<Path d="M46.4904 41.2448L42.9846 41.2448V44.7506H46.4904V41.2448Z" fill={outline ? "black" : undefined} />
		<Path d="M46.4904 37.7389L42.9846 37.7389V41.2448L46.4904 41.2448V37.7389Z" fill={outline ? "black" : undefined} />
		<Path d="M46.4904 34.233H42.9846V37.7389L46.4904 37.7389V34.233Z" fill={outline ? "black" : undefined} />
		<Path d="M49.9963 30.7272H46.4904V34.233H49.9963L49.9963 30.7272Z" fill={outline ? "black" : undefined} />
		<Path d="M53.5022 30.7272H49.9963L49.9963 34.233H53.5022L53.5022 30.7272Z" fill={outline ? "black" : undefined} />
		<Path d="M57.008 30.7272L53.5022 30.7272L53.5022 34.233H57.008V30.7272Z" fill={outline ? "black" : undefined} />
		<Path d="M60.5139 27.2213L57.008 27.2213L57.008 30.7272H60.5139V27.2213Z" fill={outline ? "black" : undefined} />
		<Path d="M60.5139 23.7155H57.008L57.008 27.2213L60.5139 27.2213V23.7155Z" fill={outline ? "black" : undefined} />
		<Path d="M57.008 20.2096H53.5022L53.5022 23.7154L57.008 23.7155V20.2096Z" fill={outline ? "black" : undefined} />
		<Path d="M53.5022 20.2096H49.9963V23.7155L53.5022 23.7154L53.5022 20.2096Z" fill={outline ? "black" : undefined} />
		<Path d="M49.9963 23.7155H46.4904V27.2213L49.9963 27.2213L49.9963 23.7155Z" fill={outline ? "black" : undefined} />
		<Path d="M46.4904 27.2213H42.9846L42.9846 30.7272L46.4904 30.7272V27.2213Z" fill={outline ? "black" : undefined} />
		<Path d="M42.9846 27.2213H39.4787V30.7272H42.9846L42.9846 27.2213Z" fill={outline ? "black" : undefined} />
		<Path d="M39.4787 23.7155L35.9729 23.7154L35.9729 27.2213H39.4787V23.7155Z" fill={outline ? "black" : undefined} />
		<Path d="M39.4787 20.2096L35.9729 20.2096V23.7154L39.4787 23.7155V20.2096Z" fill={outline ? "black" : undefined} />
		<Path d="M42.9846 16.7037L39.4787 16.7037L39.4787 20.2096H42.9846V16.7037Z" fill={outline ? "black" : undefined} />
		<Path d="M46.4904 13.1979L42.9846 13.1962L42.9846 16.7037H46.4904V13.1979Z" fill={outline ? "black" : undefined} />
		<Path d="M49.9963 9.6926L46.4904 9.69092L46.4904 13.1979H49.9963V9.6926Z" fill={outline ? "black" : undefined} />
		<Path d="M57.008 9.69303H53.5022V13.1979H57.008V9.69303Z" fill={outline ? "black" : undefined} />
		<Path d="M53.5022 9.69303L49.9963 9.6926V13.1979H53.5022V9.69303Z" fill={outline ? "black" : undefined} />
		<Path d="M60.5139 9.69303L57.008 9.69303V13.1979H60.5139V9.69303Z" fill={outline ? "black" : undefined} />
		<Path d="M64.0197 13.1979H60.5139V16.7037H64.0197L64.0197 13.1979Z" fill={outline ? "black" : undefined} />
		<Path d="M67.5256 16.7037H64.0197V20.2096H67.5256L67.5256 16.7037Z" fill={outline ? "black" : undefined} />
		<Path d="M71.0314 23.7155L67.5256 23.7155V27.2213L71.0314 27.2213V23.7155Z" fill={outline ? "black" : undefined} />
		<Path d="M71.0314 20.2096H67.5256V23.7155L71.0314 23.7155V20.2096Z" fill={outline ? "black" : undefined} />
		<Path d="M71.0314 30.7272H67.5256V34.233L71.0314 34.233V30.7272Z" fill={outline ? "black" : undefined} />
		<Path d="M71.0314 27.2213L67.5256 27.2213V30.7272H71.0314V27.2213Z" fill={outline ? "black" : undefined} />
		<Path d="M67.5256 34.233H64.0197V37.7389L67.5256 37.7389L67.5256 34.233Z" fill={outline ? "black" : undefined} />
		<Path d="M64.0197 37.7389H60.5139V41.2448L64.0197 41.2448L64.0197 37.7389Z" fill={outline ? "black" : undefined} />
		<Path d="M60.5139 41.2448H57.008V44.7506L60.5139 44.7506V41.2448Z" fill={outline ? "black" : undefined} />
		<Path d="M57.008 41.2448H53.5022V44.7506L57.008 44.7506V41.2448Z" fill={outline ? "black" : undefined} />
		<Path d="M57.008 44.7506L53.5022 44.7506V48.2565H57.008V44.7506Z" fill={outline ? "black" : undefined} />
		<Path d="M64.0197 44.7506H60.5139V48.2565H64.0197L64.0197 44.7506Z" fill={outline ? "black" : undefined} />
		<Path d="M60.5139 44.7506L57.008 44.7506V48.2565H60.5139V44.7506Z" fill={outline ? "black" : undefined} />
		<Path d="M67.5256 48.2565L64.0197 48.2565V51.7623H67.5256L67.5256 48.2565Z" fill={outline ? "black" : undefined} />
		<Path d="M71.0314 51.7623L67.5256 51.7623V55.2682H71.0314V51.7623Z" fill={outline ? "black" : undefined} />
		<Path d="M74.5373 55.2682L71.0314 55.2682V58.7741H74.5373V55.2682Z" fill={outline ? "black" : undefined} />
		<Path d="M78.0432 58.7741L74.5373 58.7741V62.2799H78.0432V58.7741Z" fill={outline ? "black" : undefined} />
		<Path d="M81.549 62.2799L78.0432 62.2799V65.7858H81.549V62.2799Z" fill={outline ? "black" : undefined} />
		<Path d="M85.0549 65.7858L81.549 65.7858V69.2916H85.0549V65.7858Z" fill={outline ? "black" : undefined} />
		<Path d="M88.5608 69.2916L85.0549 69.2916V72.7975H88.5608V69.2916Z" fill={outline ? "black" : undefined} />
		<Path d="M92.0666 72.7975L88.5608 72.7975V76.3033H92.0666L92.0666 72.7975Z" fill={outline ? "black" : undefined} />
		<Path d="M95.575 76.2678H92.0692V79.7737L95.575 79.7737V76.2678Z" fill={outline ? "black" : undefined} />
		<Path d="M95.575 83.2796H92.0692V86.7854H95.575V83.2796Z" fill={outline ? "black" : undefined} />
		<Path d="M95.575 79.7737L92.0692 79.7737V83.2796H95.575V79.7737Z" fill={outline ? "black" : undefined} />
		<Path d="M85.0574 86.8034H81.5516V90.3093H85.0574V86.8034Z" fill={outline ? "black" : undefined} />
		<Path d="M88.5633 86.8034H85.0574V90.3093H88.5633V86.8034Z" fill={outline ? "black" : undefined} />
		<Path d="M92.0692 86.8034H88.5633V90.3093H92.0692V86.8034Z" fill={outline ? "black" : undefined} />
		<Path d="M81.5516 83.2975H78.0457V86.8034H81.5516V83.2975Z" fill={outline ? "black" : undefined} />
		<Path d="M78.0432 79.8092H74.5373V83.3151L78.0432 83.3151V79.8092Z" fill={outline ? "black" : undefined} />
		<Path d="M74.5373 76.3033H71.0314V79.8092H74.5373V76.3033Z" fill={outline ? "black" : undefined} />
		<Path d="M71.0314 72.7975H67.5256V76.3034L71.0314 76.3033V72.7975Z" fill={outline ? "black" : undefined} />
		<Path d="M67.5256 69.2916H64.0197L64.0197 72.7975L67.5256 72.7975V69.2916Z" fill={outline ? "black" : undefined} />
		<Path d="M64.0197 65.7858H60.5139L60.5139 69.2917L64.0197 69.2916V65.7858Z" fill={outline ? "black" : undefined} />
		<Path d="M60.5139 62.2799H57.008V65.7858L60.5139 65.7858V62.2799Z" fill={outline ? "black" : undefined} />
		<Path d="M57.008 58.7741H53.5022V62.2799L57.008 62.2799V58.7741Z" fill={outline ? "black" : undefined} />
		<Path d="M46.4904 58.7741H42.9846V62.2799H46.4904V58.7741Z" fill={outline ? "black" : undefined} />
		<Path d="M49.9963 58.7741H46.4904V62.2799H49.9963L49.9963 58.7741Z" fill={outline ? "black" : undefined} />
		<Path d="M53.5022 58.7741H49.9963L49.9963 62.2799L53.5022 62.2799V58.7741Z" fill={outline ? "black" : undefined} />
		<Path d="M14.9352 86.8H18.441V90.3059H14.9352V86.8Z" fill={outline ? "black" : undefined} />
		<Path d="M18.441 83.2941H21.9469V86.8H18.441V83.2941Z" fill={outline ? "black" : undefined} />
		<Path d="M21.9494 79.8092H25.4553L25.4553 83.3117L21.9494 83.3151V79.8092Z" fill={outline ? "black" : undefined} />
		<Path d="M25.4553 76.3033H28.9612L28.9612 79.8058L25.4553 79.8092V76.3033Z" fill={outline ? "black" : undefined} />
		<Path d="M28.9612 72.7975H32.467L32.467 76.2999L28.9612 76.3033V72.7975Z" fill={outline ? "black" : undefined} />
		<Path d="M32.467 69.2916H35.9729L35.9729 72.7941L32.467 72.7975V69.2916Z" fill={outline ? "black" : undefined} />
		<Path d="M35.9729 65.7858H39.4787L39.4787 69.2882L35.9729 69.2916V65.7858Z" fill={outline ? "black" : undefined} />
		<Path d="M39.4787 62.2799H42.9846V65.7824L39.4787 65.7858V62.2799Z" fill={outline ? "black" : undefined} />
		<Path d="M11.4278 86.7922H7.92199L7.91946 90.296H11.4253L11.4278 86.7922Z" fill={outline ? "black" : undefined} />
		<Path d="M14.9337 86.7922H11.4278L11.4253 90.296H14.9312L14.9337 86.7922Z" fill={outline ? "black" : undefined} />
		<Path d="M7.93067 76.3034H4.4248V79.8092L7.93067 79.8092V76.3034Z" fill={outline ? "black" : undefined} />
		<Path d="M7.93067 83.3151H4.4248V86.8209H7.93067V83.3151Z" fill={outline ? "black" : undefined} />
		<Path d="M7.93067 79.8092L4.4248 79.8092V83.3151H7.93067V79.8092Z" fill={outline ? "black" : undefined} />
		<Path d="M28.9611 51.7623H32.467V55.2682H28.9612L28.9611 51.7623Z" fill={outline ? "black" : undefined} />
		<Path d="M25.4553 55.2682H28.9612V58.7741H25.4553L25.4553 55.2682Z" fill={outline ? "black" : undefined} />
		<Path d="M21.9494 58.7741H25.4553V62.2799H21.9494L21.9494 58.7741Z" fill={outline ? "black" : undefined} />
		<Path d="M18.4436 62.2799H21.9494V65.7858H18.4436L18.4436 62.2799Z" fill={outline ? "black" : undefined} />
		<Path d="M14.9377 65.7858H18.4436V69.2916H14.9377L14.9377 65.7858Z" fill={outline ? "black" : undefined} />
		<Path d="M11.4318 69.2916H14.9377V72.7975H11.4318L11.4318 69.2916Z" fill={outline ? "black" : undefined} />
		<Path d="M7.92597 72.7975H11.4318V76.3033H7.92599L7.92597 72.7975Z" fill={outline ? "black" : undefined} />
		<Path d="M35.9729 48.2565L32.467 48.2565V51.7623H35.9729V48.2565Z" fill={outline ? "black" : undefined} />
	</Svg>)