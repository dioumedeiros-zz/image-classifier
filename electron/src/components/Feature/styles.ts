import styled from "styled-components";

export const Container = styled.div`
  height: 40vh;
  width: 100%;
  background: #303846;
  color: #f1f1f1;
`;

export const Content = styled.div`
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 0.5rem 1.5rem;

  header {
    font-size: 1.2rem;
    font-weight: 600;
    text-align: center;
    padding-bottom: 0.5rem;
  }
`;

export const Wrapper = styled.div`
  width: 100%;
  display: flex;
  justify-content: space-between;
  margin-top: 2rem;
  margin-bottom: 5rem;
`;

export const Title = styled.h2`
  text-transform: uppercase;
  margin-bottom: 0.825rem;
`;

export const Subtitle = styled.h4`
  text-transform: uppercase;
  margin-bottom: 0.825rem;
  font-weight: 500;
`;

export const List = styled.div``;

export const ListItem = styled.div`
  padding: 0.1rem;
`;

export const Divider = styled.div`
  width: 100%;
  margin: 2rem auto;
  border-bottom: 2px solid #47d3ad;
`;
